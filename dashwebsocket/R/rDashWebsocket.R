# AUTO GENERATED FILE - DO NOT EDIT

#' @export
rDashWebsocket <- function(id=NULL, msg=NULL, url=NULL) {
    
    props <- list(id=id, msg=msg, url=url)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashWebsocket',
        namespace = 'dashwebsocket',
        propNames = c('id', 'msg', 'url'),
        package = 'dashwebsocket'
        )

    structure(component, class = c('dash_component', 'list'))
}
