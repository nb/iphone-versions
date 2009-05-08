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