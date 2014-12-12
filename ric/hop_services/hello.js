/*=====================================================================*/
/*    serrano/prgm/project/hop/3.0.x/examples/hello/hello.js           */
/*    -------------------------------------------------------------    */
/*    Author      :  Manuel Serrano                                    */
/*    Creation    :  Fri Apr 18 09:42:04 2014                          */
/*    Last change :  Mon Apr 21 07:09:39 2014 (serrano)                */
/*    Copyright   :  2014 Manuel Serrano                               */
/*    -------------------------------------------------------------    */
/*    basic example that shows client/server interaction               */
/*    -------------------------------------------------------------    */
/*    run: hop -v -g hello.js                                          */
/*    browser: http://localhost:8080/hop/hello                         */
/*=====================================================================*/

service helloServerDate() 
{
  return Date.now();
}

service hello() 
{
  var sdate = <TD> { id: "sdate", new Date( Date.now() ).toString() };
  var cdate = <TD> { id: "cdate", "-" };

  return <HTML> 
  {
    <BUTTON> 
    {
      onclick: ~{
        withHOP( 
          ${helloServerDate}(),
          function( snow )
          {
            ${sdate}.innerHTML = new Date( snow ).toString();
            ${cdate}.innerHTML = new Date( Date.now() ).toString();
          } 
        ) 
      },
        "Click me to update dates..."
    } 
    </BUTTON>,
      <TABLE> {
        <TR> 
        {
          <TH> { "server date:" }, sdate
        },
        <TR> 
        {
          <TH> { "client date:" }, cdate 
        }
      } </TABLE>
  }
}