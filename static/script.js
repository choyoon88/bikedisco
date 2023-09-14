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

                //Add coordinates and station infos to the locationsAndStationInfos array from citybike api
                locationsAndStationInfos.push({
                    lat: lat,
                    lng: lng,
                    name, 
                    freeBike,
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
        <button class="btn btn-outline-success" id="${buttonId}">Write a review</button>
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
                window.open(targetUrl, "_blank");
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



document.addEventListener('DOMContentLoaded', function() {
    const countryDropdown = document.getElementById('bike-station-country');
    const cityDropdown = document.getElementById('bike-station-city');
    const stationDropdown = document.getElementById('bike-station-name');

    function populateCountryDropdown() {
        Promise.all(urls.map(url => fetch(url).then(response => response.json())))            
            .then((dataArray) => {
                dataArray.forEach(data => {
                    const countries = data.network.location.country;
                    countries.forEach(country => {
                        const option = document.createElement('option');
                        option.value = country;
                        option.text = country;
                        countryDropdown.appendChild(option);
                    });
                })
            })
            .catch(error => {
                console.log('Error fetching countries:', error);
            });
    }

    function populateCityDropdown(selectedCountry) {
        Promise.all(urls.map(url => fetch(url).then(response => response.json())))
            .then((dataArray) => {
                dataArray.forEach(data => {
                    if (data.network.location.country === selectedCountry) {
                        const cities = data.network.location.city;
                        cities.forEach(city => {
                            const option = document.createElement('option');
                            option.value = city;
                            option.text = city;
                            cityDropdown.appendChild(option);
                        });
                    }
                })
            })
            .catch(error => {
                console.log('Error fetching cities:', error);
            });
    }

    function populateStationDropdown(selectedCity) {
        Promise.all(urls.map(url => fetch(url).then(response => response.json())))
            .then((dataArray) => {
                dataArray.forEach(data => {
                    if (data.network.location.city === selectedCity) {
                        const stations = data.network.stations;
                        stations.forEach(station => {
                            const option = document.createElement('option');
                            option.value = station.name;
                            option.text = station.name;
                            stationDropdown.appendChild(option);
                        });
                    }
                })
            })
            .catch(error => {
                console.log('Error fetching stations:', error);
            });
    }

    populateCountryDropdown()

    countryDropdown.addEventListener('change', function() {
        const selectedCountry = countryDropdown.value;
        if (selectedCountry) {
            populateCityDropdown(selectedCountry);
        } else {
            cityDropdown.innerHTML = '<option value="" disabled selected>Select City</option>';
            stationDropdown.innerHTML = '<option value="" disabled selected>Select Station</option>';
        }
    });

    cityDropdown.addEventListener('change', function() {
        const selectedCity = cityDropdown.value;
        if (selectedCity) {
            populateStationDropdown(selectedCity);
        } else {
            stationDropdown.innerHTML = '<option value="" disabled selected>Select Station</option>';
        }
    });
});



// let stationLocationInfo = [];

// function fetchDataFromAPI(url) {
//     return fetch(url)
//     .then(response => response.json())
//     .then(data => {
//         const country = data.network.location.country;
//         const city = data.network.location.city;
//         const stations = data.network.stations.map(station => station.name);

//         return { country, city, stations }
//     })
//     .catch((error) => {
//         console.error("Error fetching location data:", error);
//     });
// }

