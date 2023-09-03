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

        let contentString = `<strong>${locationsAndStationInfos[i].name}</strong><p>Free Bikes: ${locationsAndStationInfos[i].freeBike}</p>`

        // Adding infowindow basic code structure reference: https://developers.google.com/maps/documentation/javascript/infowindows
        const infowindow = new google.maps.InfoWindow({
            content: contentString,
        });

        marker.addListener("click", () => {
            infowindow.open({
                anchor: marker,
                map,
            });
        });

        markers.push(marker);
    }
    // Use MarkerClusterer to create marker clusters
    new MarkerClusterer(map, markers, {
        imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m",
    });
}
