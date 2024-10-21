// 제이쿼리 선언 - 공공데이터에서 받은 서버 주소에서 정보 연결
$(function(){

  $("#searchBtn").click(function(){
    alert("검색버튼 클릭");
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=Nv9RTCwmBG8an0doksPYFfB8I%2FkW3%2BZeXgcPhk1uh%2BzI%2FoYjr1m9RYXgPwwYDwWzAu8jg3IfmyNWrE%2FGNSyC4A%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;
    $.ajax({
      url:surl,
      type:"get",
      data:"",
      datatype:"json",
      success:function(data){
        alert("성공");
        console.log(data);
        // console.log(data.response.body.items.item);
        var p_item = data.response.body.items.item;
        var p_data = "";
        for(var i=0;i<p_item.length;i++){
          count++;

          p_data += `<tr id='${p_item[i].galContentId}'>`;
          p_data += `<td>${p_item[i].galContentId}</td>`;
          p_data += `<td>${p_item[i].galTitle}</td>`;
          p_data += `<td>${p_item[i].galPhotographer}</td>`;
          p_data += `<td>${p_item[i].galModifiedtime}</td>`;
          p_data += `<td><img src='${p_item[i].galWebImageUrl}'></td>`;
          p_data += `</tr>`;

        }
        $("#tbody").html(p_data);

      },
      error:function(){
        alert("실패");
      }
    });
  });
});