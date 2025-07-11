#' @method plot mrelnet
#' @param type.coef If \code{type.coef="2norm"} then a single curve per
#' variable, else if \code{type.coef="coef"}, a coefficient plot per response
#' @rdname plot.glmnet
#' @export
plot.mrelnet <-
  function(x, xvar=c("lambda","norm","dev"),label=FALSE,type.coef=c("coef","2norm"),...){
    type.coef=match.arg(type.coef)
    xvar=match.arg(xvar)
    beta=x$beta
    if(xvar=="norm") {
      cnorm1=function(beta){
        which=nonzeroCoef(beta)
        beta=as.matrix(beta[which,])
        apply(abs(beta),2,sum)
      }
      norm=apply(sapply(x$beta,cnorm1),1,sum)
    } else norm = NULL
    dfmat=x$dfmat
    if(type.coef=="coef"){
      ncl=nrow(dfmat)
      clnames=rownames(dfmat)
      for( i in seq(ncl)){
        plotCoef(beta[[i]],norm,x$lambda,dfmat[i,],x$dev.ratio,label=label,xvar=xvar,ylab=paste("Coefficients: Response",clnames[i]),...)
      }
    }
    else
        plotCoef(coefnorm(beta,2),norm,x$lambda,dfmat[1,],x$dev.ratio,label=label,xvar=xvar,ylab="Coefficient 2Norms",...)

  }
