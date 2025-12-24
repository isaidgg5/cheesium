/**
HTML5 YouTube Embedder
By: Dickson Law
(C) 2014 GameGeisha Interactive
**/

var __gms_youtube__ = new Array();
var __gms_logo__ = new Array();
var __gms_game_area__ = document.getElementById('gm4html5_div_id');
var __gms_game_canvas__ = document.getElementById('canvas');

var outside = 0;
__gms_game_canvas__.setAttribute("onmouseout","mouseLeave()")
__gms_game_canvas__.setAttribute("onmouseover","mouseEnter()")

function mouseLeave()
{
	outside=1
	//return outside
}


function mouseEnter()
{
	outside=0
	//return outside
}


function getOutside()
{
	
	return outside
}

function youtube_show(video_id, x, y, width, height, allow_fullscreen) {
	var to_embed = document.createElement('video');
	to_embed.setAttribute("style", "position:absolute;z-index:" + (__gms_game_canvas__.style.zIndex+1) + ";");
	to_embed.setAttribute("width", width);
	to_embed.setAttribute("height", height);
	to_embed.setAttribute("frameborder", 0);
	to_embed.setAttribute("autoplay", 1)
	to_embed.setAttribute("src", video_id);
	to_embed.setAttribute("onclick", "openLink()");

	
	var added = __gms_game_area__.appendChild(to_embed);
	added.style.left = x + "px";
	added.style.top = y + "px";
	return __gms_youtube__.push(added)-1;
}

function logo_show(video_id, x, y, width, height, allow_fullscreen) {
	var to_embed = document.createElement('video');
	to_embed.setAttribute("style", "position:absolute;z-index:" + (__gms_game_canvas__.style.zIndex+1) + ";");
	to_embed.setAttribute("width", width);
	to_embed.setAttribute("height", height);
	to_embed.setAttribute("frameborder", 0);
	to_embed.setAttribute("autoplay", 1)
	to_embed.setAttribute("onclick", "openLogo()");

	
	var added = __gms_game_area__.appendChild(to_embed);
	added.style.left = x + "px";
	added.style.top = y + "px";
	return __gms_logo__.push(added)-1;
}
function openLogo(){
	window.open("http://seanmombo.com",'_blank');
}

function openLink(){
	window.open("http://armor.ag/MoreGames",'_blank');
}

function openFb(){
	window.open("http://www.facebook.com/ArmorGames",'_blank');
}

function youtube_close(handle) {
	__gms_game_area__.removeChild(__gms_youtube__[handle]);
}
function logo_close(handle) {
	__gms_game_area__.removeChild(__gms_logo__[handle]);
}
function youtube_get_x(handle) {
	return parseInt(__gms_youtube__[handle].style.left);
}

function youtube_set_x(handle, new_x) {
	__gms_youtube__[handle].style.left = new_x + "px";
}

function youtube_get_y(handle) {
	return parseInt(__gms_youtube__[handle].style.top);
}

function youtube_set_y(handle, new_y) {
	__gms_youtube__[handle].style.top = new_y + "px";
}

function youtube_get_height(handle) {
	return parseInt(__gms_youtube__[handle].getAttribute("height"));
}

function youtube_set_height(handle, new_h) {
	__gms_youtube__[handle].setAttribute("height", new_h);
}

function youtube_get_width(handle) {
	return parseInt(__gms_youtube__[handle].getAttribute("width"));
}

function youtube_set_width(handle, new_w) {
	__gms_youtube__[handle].setAttribute("width", new_w);
}