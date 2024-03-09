function dor(i) {
	console.log(i);
	if (i <= 0) {
  	return 'dor';
  }
  	dor(i-1)+1;

}

ocd = dor(5)

console.log(ocd)






















function dor(lst) {
	//console.log(lst);
	if (lst == []) {
  	return '';
  }
  else if (lst.length == 1) {
  	return lst[0];
  }
  
  mau = dor(lst.slice(1));
  ocd = lst[0];
  
  //console.log(mau);
  //console.log(ocd);
  //console.log(dor)
  
  if (mau > ocd) { //estava a dar o 1º elemento de todos antes porque em vez de ocd, tinha aqui dor
  	return mau;
  }
  else {
  	return ocd;
  }
}

ocd = dor([3, 2, 0, -1, 29, 6]);
console.log(ocd)