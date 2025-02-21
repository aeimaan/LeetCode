class EventEmitter {
    constructor(){
        this.events = new Map();
        this.subscriptions = [];
    }
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (!this.events.has(eventName)){ // event has no subscribers
            this.events.set(eventName, []);
        }
        const arr = this.events.get(eventName);
        arr.push(callback);

        // const subscriptionIndex = this.subscriptions.length;
        // this.subscriptions.push({eventName, callback})
        return {
            unsubscribe: () => {
                const arr = this.events.get(eventName);
                if (!arr) return;
                const idx = arr.indexOf(callback)
                if (idx !== -1){ //found 
                    arr.splice(idx, 1);
                }
                // this.subscriptions[subscriptionIndex] = null;
                return undefined;
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const arr = this.events.get(eventName);
        if (!arr){
            return [];
        }
        const results = []
        for (const cb of arr){
            results.push(cb(...args)) //call the call backs with args, then push onto res
        }
        return results;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */