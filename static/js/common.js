function set_cookie(name, value) {
	var expiredays = 365;
	var exdate = new Date();
	exdate.setDate(exdate.getDate()+expiredays);
	document.cookie = name + "=" +encodeURI(value) + ";expires="+exdate.toGMTString() + "; path=/";
}

function get_cookie(name) {
	if (document.cookie.length <= 0) return '';
  start = document.cookie.indexOf(name + "=");
  if (start == -1) return '';
	value_start = start + name.length + 1;
  end = document.cookie.indexOf(";", value_start);
	if (end == -1) end = document.cookie.length;
  return decodeURI(document.cookie.substring(value_start, end));
}

Number.prototype.toRad = function() {  // convert degrees to radians
  return this * Math.PI / 180;
}

Number.prototype.toDeg = function() {  // convert radians to degrees (signed)
  return this * 180 / Math.PI;
}

function distance(start, end) {
	function convert(o) {
		if (o.coords)
			return {latitude: o.coords.latitude, longitude: o.coords.longitude}
		else
			return o;
	}
	start = convert(start)
	end = convert(end)
	var R = 6371; // earth's mean radius in km
	return Math.acos(Math.sin(start.latitude.toRad())*Math.sin(end.latitude.toRad()) +
	                  Math.cos(start.latitude.toRad())*Math.cos(end.latitude.toRad()) *
	                  Math.cos((end.longitude - start.longitude).toRad())) * R;
}