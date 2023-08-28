var locations = [];

fetch("https://api.citybik.es/v2/networks/dublinbikes")
    .then((response) => response.json())
    .then((data) => {
        const stations = data.network.stations;

        stations.forEach((station) => {
            const lat = station.latitude;
            const lng = station.longitude;

            locations.push({
                lat: lat,
                lng: lng
            }); //Add coordinates to the location array from citybike api
        });

        initMap();
    })
    .catch((error) => {
        console.error("Error fetching data:", error);
    });

function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: {
            lat: locations[0].lat,
            lng: locations[0].lng
        }
    });

    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var markers = [];

    // Add markers to the map using the locations array
    for (var i = 0; i < locations.length; i++) {
        var marker = new google.maps.Marker({
            position: locations[i],
            label: labels[i % labels.length]
        });
        markers.push(marker);
    }

    // Use MarkerClusterer to create marker clusters
    new MarkerClusterer(map, markers, {
        imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m",
    });
}