function resistador (res, numerador) {
	if(numerador<=0) return 0;
  else if(numerador==1) {
  	return 3*res;
  }
  //else if(numerador==2){
  //	return 1/(1/(3*res)+1/res) + 2*res;		// = return 1/(1/reistador(res, numerador-1)+1/res) + 2*res
  //}
  else {
  	return 1/(1/resistador(res, numerador-1) + 1/res + 2*res);
  }
}

console.log(resistador(5, 1000))