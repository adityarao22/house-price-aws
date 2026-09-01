const form = document.getElementById("predictionForm");
const result = document.getElementById("result");

const API_URL =
    "Your_API_INVOKE_URL/predict";

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    result.innerHTML = "Predicting...";

    const data = {
        area: Number(document.getElementById("area").value),
        bedrooms: Number(document.getElementById("bedrooms").value),
        bathrooms: Number(document.getElementById("bathrooms").value),
        stories: Number(document.getElementById("stories").value),
        parking: Number(document.getElementById("parking").value),

        mainroad: Number(document.getElementById("mainroad").value),
        guestroom: Number(document.getElementById("guestroom").value),
        basement: Number(document.getElementById("basement").value),
        hotwaterheating: Number(
            document.getElementById("hotwaterheating").value
        ),
        airconditioning: Number(
            document.getElementById("airconditioning").value
        ),
        furnishingstatus: Number(
            document.getElementById("furnishingstatus").value
        )
    };

    console.log("Sending:", data);

    try {

        const response = await fetch(API_URL, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)
        });

        const responseText = await response.text();

        console.log("API response:", responseText);

        const output = JSON.parse(responseText);

        if (!response.ok) {
            throw new Error(output.error || "API request failed");
        }

        const price = Number(output.predicted_price);

        if (Number.isNaN(price)) {
            throw new Error(
                "API returned an invalid predicted price"
            );
        }

        result.innerHTML =
            "Predicted Price: ₹ " +
            price.toLocaleString("en-IN");

    } catch (error) {

        console.error("Prediction error:", error);

        result.innerHTML =
            "Error: " + error.message;
    }
});