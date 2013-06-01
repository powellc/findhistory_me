var map = L.mapbox.map('map', 'jacques.map-612s2qsj').setView([44.8011, -68.7783], 15);

function onEachFeature(feature, layer) {
  var popupContent = "<p>I started out as a GeoJSON " +
    feature.geometry.type + ", but now I'm a Leaflet vector!</p>";

  if (feature.properties && feature.properties.popupContent) {
    popupContent += feature.properties.popupContent;
  }

  layer.bindPopup(popupContent);
}

L.geoJson(data, {
  style: function (feature) {
    return feature.properties && feature.properties.style;
  },

  onEachFeature: onEachFeature,

  pointToLayer: function (feature, latlng) {
    return L.circleMarker(latlng, {
      radius: 8,
      fillColor: "#ff7800",
      color: "#000",
      weight: 1,
      opacity: 1,
      fillOpacity: 0.8
    });
  }

}).addTo(map);
