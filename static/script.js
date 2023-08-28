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
    "https://api.citybik.es/v2/networks/santander-cycles",
    "https://api.citybik.es/v2/networks/nextbike-university-of-surrey",
    "https://api.citybik.es/v2/networks/santander-cycles",
    "https://api.citybik.es/v2/networks/co-bikes-exeter",
    "https://api.citybik.es/v2/networks/belfastbikes-belfast",

]

Promise.all(urls.map(url => fetch(url).then(response => response.json())))
    .then((dataArray) => {
        const locations = [];
        dataArray.forEach(data => {
            const stations = data.network.stations;

            stations.forEach((station) => {
                const lat = station.latitude;
                const lng = station.longitude;

                locations.push({
                    lat: lat,
                    lng: lng
                }); //Add coordinates to the location array from citybike api
            })
        });

        initMap(locations);
    })
    .catch((error) => {
        console.error("Error fetching data:", error);
    });

function initMap(locations) {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 6,
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