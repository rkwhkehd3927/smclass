

// ################### 4. 이벤트 페이지 url 복사 
// 현재 url 변수로 가져오기
let nowUrl = window.location.href;
function copyUrl(){
  // alert("테스트")
  // nowUrl 변수에 담긴 주소
  navigator.clipboard.writeText(nowUrl).then(res=>{
    alert("주소가 복사되었습니다.");
  })
}
