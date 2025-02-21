class EventEmitter {
  constructor() {
    // Map from event name -> array of callbacks
    this.events = new Map();
    // Global list of all subscriptions in chronological order
    this.subscriptions = [];
  }

  /**
   * @param {string} eventName
   * @param {Function} callback
   * @return {Object} with { unsubscribe() }
   */
  subscribe(eventName, callback) {
    // 1) Add callback to the event's array
    if (!this.events.has(eventName)) {
      this.events.set(eventName, []);
    }
    const arr = this.events.get(eventName);
    arr.push(callback);

    // 2) Add to global subscriptions
    const index = this.subscriptions.length;
    this.subscriptions.push({ eventName, callback });

    // 3) Return an object with unsubscribe
    return {
      unsubscribe: () => {
        // remove from the event array
        const arr = this.events.get(eventName);
        if (!arr) return undefined;
        const idx = arr.indexOf(callback);
        if (idx !== -1) {
          arr.splice(idx, 1);
        }
        // mark global subscription as removed
        this.subscriptions[index] = null;
        return undefined;
      }
    };
  }

  /**
   * Unsubscribe by global index
   * @param {number} globalIndex
   * @return {undefined}
   */
  unsubscribe(globalIndex) {
    const sub = this.subscriptions[globalIndex];
    if (!sub) {
      return undefined; // already unsubscribed or invalid
    }
    const { eventName, callback } = sub;
    // remove from the event array
    const arr = this.events.get(eventName);
    if (arr) {
      const idx = arr.indexOf(callback);
      if (idx !== -1) {
        arr.splice(idx, 1);
      }
    }
    // mark it unsubscribed
    this.subscriptions[globalIndex] = null;
    return undefined;
  }

  /**
   * @param {string} eventName
   * @param {Array} args
   * @return {Array}
   */
  emit(eventName, args = []) {
    const arr = this.events.get(eventName);
    if (!arr) {
      return [];
    }
    const results = [];
    for (const cb of arr) {
      results.push(cb(...args));
    }
    return results;
  }
}
