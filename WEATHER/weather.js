const API_KEY = "258578c254db31bf60e8d773a6e5961a";

const cityInput = document.getElementById("cityInput");
const searchBtn = document.getElementById("searchBtn");

const city = document.getElementById("city");
const temperature = document.getElementById("temperature");
const description = document.getElementById("description");
const feelsLike = document.getElementById("feelsLike");
const humidity = document.getElementById("humidity");
const wind = document.getElementById("wind");
const weatherIcon = document.getElementById("weatherIcon");
const error = document.getElementById("error");

async function getWeather(cityName) {

    if (!cityName) {
        error.textContent = "Please enter a city name.";
        return;
    }

    error.textContent = "Loading...";

    const url =
        `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(cityName)}&appid=${API_KEY}&units=metric`;

    try {

        const response = await fetch(url);

        const data = await response.json();

        console.log("API Response:", data);

        if (!response.ok) {
            throw new Error(data.message || "Weather request failed");
        }

        // City
        city.textContent =
            `${data.name}, ${data.sys.country}`;

        // Temperature
        temperature.textContent =
            `${Math.round(data.main.temp)}°C`;

        // Description
        description.textContent =
            data.weather[0].description;

        // Feels like
        feelsLike.textContent =
            `${Math.round(data.main.feels_like)}°C`;

        // Humidity
        humidity.textContent =
            `${data.main.humidity}%`;

        // Wind
        wind.textContent =
            `${Math.round(data.wind.speed * 3.6)} km/h`;

        // Weather icon
        const iconCode =
            data.weather[0].icon;

        weatherIcon.src =
            `https://openweathermap.org/img/wn/${iconCode}@2x.png`;

        weatherIcon.alt =
            data.weather[0].description;

        error.textContent = "";

    } catch (err) {

        console.error("Weather Error:", err);

        error.textContent =
            `Error: ${err.message}`;

        city.textContent = "--";
        temperature.textContent = "--°C";
        description.textContent = "--";
        feelsLike.textContent = "--°C";
        humidity.textContent = "--%";
        wind.textContent = "-- km/h";
        weatherIcon.src = "";
    }
}


// Search button
searchBtn.addEventListener("click", () => {

    const cityName =
        cityInput.value.trim();

    getWeather(cityName);

});


// Press Enter
cityInput.addEventListener("keypress", (event) => {

    if (event.key === "Enter") {

        getWeather(
            cityInput.value.trim()
        );

    }

});
