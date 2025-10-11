

// Function that takes another function as an argument (callback)
function greet(name, callback) {
    console.log("Hello, " + name + "!");
    callback();
  }
  
  // Callback function
  function sayGoodbye() {
    console.log("Goodbye!");
  }
  
  // Calling the greet function with the sayGoodbye function as a callback
  greet("Alice", sayGoodbye);
  