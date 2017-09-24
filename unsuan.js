function unsuan(s, a) {
	sw = "jmmh.net|jmydm.com|iieye.cc|iibq.com|bobolele.com|jmymh.com|blgl8.com|iieye.net|manhua.li|jmymh.net|aacomic.com|hrcomic.com|8mod.com|3909.net|99manga.com|cococomic.com|99manga.com|hhcomic.com|9manga.com|99mh.com|dmeden.net|dmeden.com|99comic.com|1mh.com|ddmm.cc|aacomic.com|hhmanhua.com|blmanhua.com";
	su = 'www.jmydm.com'.toLowerCase();
	b = false;
	for (i = 0; i < sw.split("|").length; i++) {
		if (su.indexOf(sw.split("|")[i]) > -1) {
			b = true;
			break
		}
	}
	if (!b)
		return "";
	k = a.substring(0, a.length - 1);
	f = a.substring(a.length - 1);
	for (i = 0; i < k.length; i++) {
		eval("s=s.replace(/" + k.substring(i, i + 1) + "/g,'" + i + "')")
	}
	ss = s.split(f);
	s = "";
	for (i = 0; i < ss.length; i++) {
		s += String.fromCharCode(ss[i])
	}
	return s
}
