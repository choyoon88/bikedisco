const urls = [
    "https://api.citybik.es/v2/networks/dublinbikes",
    "https://api.citybik.es/v2/networks/cork",
    "https://api.citybik.es/v2/networks/waterford",
    "https://api.citybik.es/v2/networks/galway",
    "https://api.citybik.es/v2/networks/limerick",
    "https://api.citybik.es/v2/networks/nextbike-glasgow",
    "https://api.citybik.es/v2/networks/nextbike-stirling",
    "https://api.citybik.es/v2/networks/santander-cycles-mk-milton-keynes",
    "https://api.citybik.es/v2/networks/santander-cycles-swansea-swansea-university",
    "https://api.citybik.es/v2/networks/santander-brunel",
    "https://api.citybik.es/v2/networks/nextbike-university-of-surrey",
    "https://api.citybik.es/v2/networks/santander-cycles",
    "https://api.citybik.es/v2/networks/co-bikes-exeter",
    "https://api.citybik.es/v2/networks/belfastbikes-belfast",
]

Promise.all(urls.map(url => fetch(url).then(response => response.json())))
    .then((dataArray) => {
        console.log("API Data:", dataArray);
        const locationsAndStationInfos = [];

        dataArray.forEach(data => {
            const stations = data.network.stations;

            stations.forEach((station) => {
                const lat = station.latitude;
                const lng = station.longitude;
                const name = station.name;
                const freeBike = station.free_bikes;
                const emptySlots = station.empty_slots;

                //Add coordinates and station infos to the locationsAndStationInfos array from citybike api
                locationsAndStationInfos.push({
                    lat: lat,
                    lng: lng,
                    name,
                    freeBike,
                    emptySlots,
                });
            })
        });

        initMap(locationsAndStationInfos);
    })
    .catch((error) => {
        console.error("Error fetching data:", error);
    });


function initMap(locationsAndStationInfos) {

    let map = new google.maps.Map(document.getElementById("map"), {
        zoom: 6,
        center: {
            lat: locationsAndStationInfos[0].lat,
            lng: locationsAndStationInfos[0].lng
        }
    });

    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var markers = [];


    for (let i = 0; i < locationsAndStationInfos.length; i++) {

        let marker = new google.maps.Marker({
            position: locationsAndStationInfos[i],
            label: labels[i % labels.length]
        });

        let buttonId = `custom-btn-${i}`;

        let contentString = `
        <strong>${locationsAndStationInfos[i].name}</strong>
        <p>Free Bikes: ${locationsAndStationInfos[i].freeBike}</p>
        <br>
        <button class="btn btn-outline-success" id="${buttonId}">Write Review</button>
        `;

        // Adding infowindow basic code structure reference: https://developers.google.com/maps/documentation/javascript/infowindows
        const infowindow = new google.maps.InfoWindow({
            content: contentString,
        });

        marker.addListener("click", () => {
            infowindow.open(map, marker);

            // Add a click event listener to the button inside the info window
            const button = document.getElementById(buttonId);
            button.addEventListener("click", () => {
                window.open(targetUrl, '_self');
            });
        });

        markers.push(marker);

        map.addListener("click", () => {
            infowindow.close();
        });
    }
    // Use MarkerClusterer to create marker clusters
    new MarkerClusterer(map, markers, {
        imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m",
    });
}

// Functions for creating Dropdown menu by fetching data from the API
document.addEventListener('DOMContentLoaded', function () {
    const countryDropdown = document.getElementById('bike-station-country');
    const cityDropdown = document.getElementById('bike-station-city');
    const stationDropdown = document.getElementById('bike-station-name');

    let stationData; // Store the fetched station data

    function fetchStationData() {
        Promise.all(urls.map(url => fetch(url).then(response => response.json())))
            .then((dataArray) => {
                stationData = dataArray;
                populateCountryDropdown();
            })
            .catch(error => {
                console.log('Error fetching data:', error);
            });
    }

    function populateCountryDropdown() {
        // Extract unique country names from the station data
        const uniqueCountries = [...new Set(stationData.flatMap(data => data.network.location.country))];

        // Populate the country dropdown
        uniqueCountries.forEach(country => {
            const option = document.createElement('option');
            option.value = country;
            option.text = country;
            countryDropdown.appendChild(option);
        });
    }

    function populateCityDropdown(selectedCountry) {
        // Extract unique city names based on the selected country
        const uniqueCities = stationData
            .filter(data => data.network.location.country === selectedCountry)
            .flatMap(data => data.network.location.city);

        // Populate the city dropdown
        cityDropdown.innerHTML = '<option value="" disabled selected>Select City</option>';
        uniqueCities.forEach(city => {
            const option = document.createElement('option');
            option.value = city;
            option.text = city;
            cityDropdown.appendChild(option);
        });
    }

    function populateStationDropdown(selectedCity) {
        // Extract station names based on the selected city
        const stationNames = stationData
            .filter(data => data.network.location.city === selectedCity)
            .flatMap(data => data.network.stations.map(station => station.name));

        // Populate the station dropdown
        stationDropdown.innerHTML = '<option value="" disabled selected>Select Station</option>';
        stationNames.forEach(station => {
            const option = document.createElement('option');
            option.value = station;
            option.text = station;
            stationDropdown.appendChild(option);
        });
    }

    // Fetch the station data when the page loads
    fetchStationData();

    countryDropdown.addEventListener('change', function () {
        const selectedCountry = countryDropdown.value;
        if (selectedCountry) {
            populateCityDropdown(selectedCountry);
        } else {
            cityDropdown.innerHTML = '<option value="" disabled selected>Select City</option>';
            stationDropdown.innerHTML = '<option value="" disabled selected>Select Station</option>';
        }
    });

    cityDropdown.addEventListener('change', function () {
        const selectedCity = cityDropdown.value;
        if (selectedCity) {
            populateStationDropdown(selectedCity);
        } else {
            stationDropdown.innerHTML = '<option value="" disabled selected>Select Station</option>';
        }
    });
});


// Function to allow 'Write Review' button from the reviews page
const reviewBtn = document.getElementById("review-btn");

reviewBtn.addEventListener('click', () => {
    window.open(targetUrl, '_self');
})