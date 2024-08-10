// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-app.js";
import { getDatabase, ref, set } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyAmtkqrD36_TJcJkMt8HvkcRSB075pxc6o",
    authDomain: "python1-39843.firebaseapp.com",
    projectId: "python1-39843",
    storageBucket: "python1-39843.appspot.com",
    messagingSenderId: "238032832771",
    appId: "1:238032832771:web:d25ce7ef4a19104fa18136",
    measurementId: "G-7D9GTCZ9F0",
    // The value of `databaseURL` depends on the location of the database
    databaseURL: "https://python1-39843-default-rtdb.firebaseio.com",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);

// Handle form submission
document.getElementById('paymentForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const paymentDate = document.getElementById('paymentDate').value;

    // Create a unique key for each entry
    const userId = new Date().getTime().toString();

    // Write to Realtime Database
    set(ref(database, 'payments/' + userId), {
        email: email,
        paymentDate: paymentDate
    })
        .then(() => {
            alert('Payment information saved successfully!');
        })
        .catch((error) => {
            alert('Failed to save payment information: ' + error);
        });
});
