// Evento que se dispara al cargar la página web
document.addEventListener("DOMContentLoaded", iniciar);

// Función que se invoca con el disparo de "DOMContentLoaded"
function iniciar() {

    // Objeto del mapa Leaflet
    var mapa = L.map('mapaid').setView([9.5, -84], 8);

    // Capa base de Carto
    var positromap = L.tileLayer(
        "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png",
        {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
            subdomains: "abcd",
            maxZoom: 20,
        }
    ).addTo(mapa);

    // Capa base de OSM
    var osm = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    });

    // Capa base de ESRI
    var esriworld = L.tileLayer(
        "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        {
            attribution: "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
        }
    );

    // Objeto de capas base
    var mapasbase = {
        "Carto Positron": positromap,
        OpenStreetMap: osm,
        "ESRI WorldImagery": esriworld,
    };

    // Control de capas
    var control_capas = L.control.layers(mapasbase, null, { collapsed: false }).addTo(mapa);

    // Control de escala
    L.control.scale().addTo(mapa);

    // Función que agrega los datos GeoJSON al mapa
    const agregarEstacionesSirgasAlMapa = (json) => {
        var estacionessirgas = L.geoJSON(json, {
            onEachFeature: function (feature, layer) {
                var popupText = `<strong>Nombre estación</strong>: ${feature.properties.name}<br>` +
                                `<strong>Tipo monumento</strong>: ${feature.properties.monument_type}<br>` +
                                `<strong>Instalada en</strong>: ${feature.properties.installed_on}<br>`;
                layer.bindPopup(popupText);
            }
        }).addTo(mapa);

        // Capa de puntos agrupados
        var estacionessirgas_agrupadas = L.markerClusterGroup({
            spiderfyOnMaxZoom: true,
        });
        estacionessirgas_agrupadas.addLayer(estacionessirgas);
        estacionessirgas_agrupadas.addTo(mapa);
        control_capas.addOverlay(estacionessirgas_agrupadas, "Estaciones SIRGAS (agrupadas)");

        // Capa de calor (heatmap)
        var coordenadas = json.features.map((feat) => [feat.geometry.coordinates[1], feat.geometry.coordinates[0]]);
        var estaciones_sirgas_calor = L.heatLayer(coordenadas, { radius: 60, blur: 1 }).addTo(mapa);
        control_capas.addOverlay(estaciones_sirgas_calor, "Estaciones SIRGAS (calor)");

        // Se agregan los datos GeoJSON al mapa
        control_capas.addOverlay(estacionessirgas, "Estaciones SIRGAS");
    };

    // Llamado a fetchGetRequest()
    fetchGetRequest('/api/v1/estacionsirgas', agregarEstacionesSirgasAlMapa);
}

// Función asíncrona que realiza una solicitud HTTP (tipo GET) a una URL especificada
const fetchGetRequest = async (url, func) => {
    try {
        const response = await fetch(url);
        const json = await response.json();
        func(json);
    } catch (error) {
        console.log(error.message);
    }
};
