const startPrivacyEngine = () => {
    // Send a request to the Python script to start the privacy engine
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/start');
    xhr.onload = () => {
        if (xhr.status === 200) {
            console.log('Privacy engine started');
        } else {
            console.error('Failed to start privacy engine');
        }
    };
    xhr.send();
};

const stopPrivacyEngine = () => {
    // Send a request to the Python script to stop the privacy engine
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/stop');
    xhr.onload = () => {
        if (xhr.status === 200) {
            console.log('Privacy engine stopped');
        } else {
            console.error('Failed to stop privacy engine');
        }
    };
    xhr.send();
};