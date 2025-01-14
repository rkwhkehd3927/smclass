var map;
    var InfoWindow,marker;
    var content,content1,content2,content3,rect;
    var url,lat,lon,name;
	var Clicklat,Clicklon;
	var result,resultDiv; 
    var centerlat,centerlon;
	var poiId,color;
	var poiId2,color2;
	var tData = new Tmapv2.extension.TData();
	let isSquareMapActive = false;
	let isAutoTrafficActive = false;
	let isMeasureDistanceActive = false; // 플래그 변수 추가
    let lastclicktime = 0;
    let lastclickx,lastclicky = 0;
    let currentDate = 0;
	 
     // 마커와 라벨을 저장할 배열 초기화
     var markerArr = [];
     var labelArr = [];

     var positions = [
    {
        title: '티맵모빌리티', 
        lonlat: new Tmapv2.LatLng(37.56520450, 126.98702028),
        keyword: '크리스마스'
    },
    {
        title: 'SKT타워', 
        lonlat: new Tmapv2.LatLng(37.566369,126.984895),
        keyword: '와인/바'
    },
    {
        title: '경찰서', 
        lonlat: new Tmapv2.LatLng(37.563709,126.989577),
        keyword: '비건식당'
    },
    {
        title: '호텔',
        lonlat: new Tmapv2.LatLng(37.565138,126.983655),
        keyword: '연말파티'
    },
    {
        title: '병원',
        lonlat: new Tmapv2.LatLng(37.565128,126.988830),
        keyword: '브런치'
    }
];
     function initTmap(){
        // map 생성
        // Tmap.map을 이용하여, 지도가 들어갈 div, 넓이, 높이를 설정합니다.
        map = new Tmapv2.Map("map_div", {
            center : new Tmapv2.LatLng(37.56520450, 126.98702028), // 지도 초기 좌표
            zoom : 16,
            width : "70%", // map의 width 설정
            height : "700px" // map의 height 설정   
        });
    
        map.addListener("click", onClick);


        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                var lat = position.coords.latitude;
                var lon = position.coords.longitude;
                centerlat = lat;
                centerlon = lon;
                console.log(lat, lon);
    
                // 마커 생성 시, icon 속성에 새로운 이미지 경로 설정
                marker = new Tmapv2.Marker({
                    position: new Tmapv2.LatLng(lat, lon),
                    map: map,
                    icon: "/static/images/markerStar.png",  // 마커 이미지 변경
                    iconSize: new Tmapv2.Size(24, 35) // 마커 이미지 크기 설정 (필요시 조정)
                });
    
                map.setCenter(new Tmapv2.LatLng(lat, lon));
                map.setZoom(16);

                updateMapCenter();
            });
        }

        // 지도 이동 이벤트 리스너 추가
        map.addListener("dragend", function() {
        updateMapCenter();
        });
    
        // 기본 상태로 measureDistance 실행
        measureDistance();
    }

    // 기본 정보
    function measureDistance() {
    resetActiveStates(); // 다른 기능 초기화
    isMeasureDistanceActive = true; // measureDistance 활성화

    $(".api_etc_btns > div#measureDistance").addClass("__color_blue_fill");
    $("#map_wrap").html('');
    }


    // 날씨 코드와 설명 매핑
const weatherDescriptions = {
    0: "맑음",
    1: "비",
    2: "비/눈",
    3: "눈",
    4: "소나기",
    5: "이슬비",
    6: "비와 눈 날림",
    7: "눈날림"
};

// 풍향 코드와 설명 매핑
function getWindDirection(degrees) {
    if (degrees >= 337.5 || degrees < 22.5) return "북풍";
    if (degrees >= 22.5 && degrees < 67.5) return "북동풍";
    if (degrees >= 67.5 && degrees < 112.5) return "동풍";
    if (degrees >= 112.5 && degrees < 157.5) return "남동풍";
    if (degrees >= 157.5 && degrees < 202.5) return "남풍";
    if (degrees >= 202.5 && degrees < 247.5) return "남서풍";
    if (degrees >= 247.5 && degrees < 292.5) return "서풍";
    if (degrees >= 292.5 && degrees < 337.5) return "북서풍";
    return ""; // 기본값
}

function updateMapCenter() {
    var center = map.getCenter();
    centerlat = center.lat();
    centerlon = center.lng();
    console.log("New center: ", centerlat, centerlon);

    readCSV('/static/기상청_격자위경도.csv', function(data) {
        let { nearestLocation_s2, locX, locY } = processCSVData(data, centerlat, centerlon);
        let { formattedDate, formattedTime } = findnow();

        lastclickx = locX; 
        lastclicky = locY;
        lastClickTime = currentDate;

        if (nearestLocation_s2) {
            const xhr = new XMLHttpRequest();
            const apiUrl = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst';
            const serviceKey = 'EPhM94JT5WuG2cnWrA7xBy4Ip1zeWGD%2Fc9StwgvLEua3LPV6Qgp9%2Bu%2Fq5hyyC9%2FtVA%2BL4WipZChsLpNs4obZ%2Bw%3D%3D';
            const queryParams = '?' + encodeURIComponent('serviceKey') + '=' + serviceKey +
                                '&' + encodeURIComponent('pageNo') + '=' + encodeURIComponent('1') +
                                '&' + encodeURIComponent('numOfRows') + '=' + encodeURIComponent('8') +
                                '&' + encodeURIComponent('dataType') + '=' + encodeURIComponent('Json') +
                                '&' + encodeURIComponent('base_date') + '=' + encodeURIComponent(formattedDate) +
                                '&' + encodeURIComponent('base_time') + '=' + encodeURIComponent(formattedTime) +
                                '&' + encodeURIComponent('nx') + '=' + encodeURIComponent(locX) +
                                '&' + encodeURIComponent('ny') + '=' + encodeURIComponent(locY);

            xhr.open('GET', apiUrl + queryParams);
            xhr.onreadystatechange = function() {
                if (this.readyState === 4) {
                    const { temperature, humidity, weather, wdDirection, wdStrength } = findSource(this.responseText);

                    const weatherDescription = weatherDescriptions[weather] || "알 수 없음";
                    const windDirection = getWindDirection(parseFloat(wdDirection));
                    const weatherIcon = `/static/images/weather${weather}.png`;

                    const weatherHTML = `
                        <div class="weather-container">
                            <div class="location">${nearestLocation_s2}</div>
                            <div class="weather-info">
                                <div class="temperature">${temperature}°</div>
                                <img src="${weatherIcon}" alt="${weatherDescription}" class="weather-icon">
                            </div>
                            </div>
                            <div class="details">
                                <div>습도 : ${humidity} %</div>
                                <div>풍향 : ${windDirection}</div>
                                <div>풍속 : ${wdStrength} m/s</div>
                            </div>
                        </div>`;
                    $(".how_we").html(weatherHTML);
                }
            };
            xhr.send('');
        }
    });
}

    
        // CSV 파일 읽기
        function readCSV(url, callback) {
            $.ajax({
                url: url,
                dataType: 'text',
                beforeSend: function(xhr) {
                    xhr.overrideMimeType('text/plain; charset=euc-kr');
                },
                success: function(data) {
                    callback(data);
                },
                error: function() {
                    alert('CSV 파일을 읽는 데 실패했습니다.');
                }
            });
        }
    
    
        // CSV 파일에서 위경도를 불러오는 함수
        function processCSVData(data, centerlat, centerlon) {
        let lines = data.split("\n");
        let minDistance = Infinity;
        let nearestLocation_s2 = '';
        let locX = 0, locY = 0;
    
        // 가장 가까운 위치 찾기
        lines.slice(1).forEach(line => {
            line = line.trim();
            if (line) {
                let [ , , 읍면동, 위도, 경도,x,y] = line.split(",");
                let distance = getDistance(centerlat, centerlon, parseFloat(위도), parseFloat(경도));
                if (distance < minDistance) {
                    minDistance = distance;
                    nearestLocation_s2 = 읍면동;
                    locX = x; // 가장 가까운 위치의 위도 저장
                    locY = y; // 가장 가까운 위치의 경도 저장
                }
            }
        });
        
        console.log(`가장 가까운 위치: ${nearestLocation_s2}, 위도: ${locX}, 경도: ${locY}`);
        return { nearestLocation_s2, locX, locY };
        }   
    
        // 거리를 계산하는 함수
        function getDistance(lat1, lon1, lat2, lon2) {
        const radius = 6371; // 지구 반지름 (km)
        let toRad = (value) => (value * Math.PI) / 180;
        let dLat = toRad(lat2 - lat1);
        let dLon = toRad(lon2 - lon1);
        let a = Math.sin(dLat / 2) ** 2 +
                Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon / 2) ** 2;
        let c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return radius * c;
        }
       
        //클릭 시점의 현재 시간을 호출하는 함수
        function findnow() {
        let currentDate = new Date();
        
        // 포맷된 날짜 (YYMMDD)
        let year = String(currentDate.getFullYear());
        let month = String(currentDate.getMonth() + 1).padStart(2, '0');
        let day = String(currentDate.getDate()).padStart(2, '0');
        let formattedDate = `${year}${month}${day}`;
    
        // 포맷된 시간 (HHMM)
        let hours = String(currentDate.getHours()).padStart(2, '0');
        let minutes = (Math.floor(currentDate.getMinutes() / 10) * 10) - 10;
        if (minutes < 0) {
            minutes = 50; // 만약 minutes이 0보다 작아지면, 50으로 설정 (한 시간 전 50분)
            hours = String(currentDate.getHours() - 1).padStart(2, '0'); // 한 시간 전
        }
        let formattedTime = `${hours}${String(minutes).padStart(2, '0')}`;
        
        console.log(formattedDate); // 예: 20241210
        console.log(formattedTime); // 예: 1930
        return { formattedDate, formattedTime };
    }
    
    
    
    
        // 기상청 API > JSON 데이터에서 필요한 정보 추출
        function findSource(responseText) {
            let data = JSON.parse(responseText);
            let items = data.response.body.items.item;
            if(!items){alert("기상청 데이터를 조회하는데 실패했습니다."); return false;}
    
            // 변수 선언 및 초기화
            let temperature = '';
            let humidity = '';
            let weather = '';
            let wdDirection = '';
            let wdStrength = '';
    
            items.forEach(item => {
                if (item.category === "PTY") {
                    weather = item.obsrValue;
                } else if (item.category === "REH") {
                    humidity = item.obsrValue;
                } else if (item.category === "T1H") {
                    temperature = item.obsrValue;
                } else if (item.category === "VEC") {
                    wdDirection = item.obsrValue;
                } else if (item.category === "WSD") {
                    wdStrength = item.obsrValue;
                }
            });
    
            return { temperature, humidity, weather, wdDirection, wdStrength };
        }

    // puzzle함수
    function onClick(e) {
        var Clicklon = e.latLng.lng();
        var Clicklat = e.latLng.lat();
       if (isSquareMapActive) {
       reverseLabel(Clicklon, Clicklat);} }
	
	function reverseLabel(Clicklon, Clicklat) {
			zoomLevel = map.getZoom();
			if (zoomLevel < 15) zoomLevel = 15;
	
			var headers = {};
			headers["appKey"] = "IOWlgu3VCB5vrfwE0YE0w3e24rgK4g612MZZEILt";
	
			$.ajax({
					method: "GET",
					headers: headers,
					url: "https://apis.openapi.sk.com/tmap/geo/reverseLabel?version=1&format=json&callback=result",
					async: false,
					data: {
							reqLevel: zoomLevel,
							centerLon: Clicklon,
							centerLat: Clicklat,
							reqCoordType: "WGS84GEO",
							resCoordType: "WGS84GEO",
					},
					success: function (response) {
							var resultInfo = response.poiInfo;
							lat = resultInfo.poiLat;
							lon = resultInfo.poiLon;
							poiId = resultInfo.id;
							name = resultInfo.name;
	
							url = `https://apis.openapi.sk.com/tmap/puzzle/pois/${poiId}?format=json&appKey=IOWlgu3VCB5vrfwE0YE0w3e24rgK4g612MZZEILt&lat=${Clicklat}&lng=${Clicklon}`;
	
							reset();
							puzzle(url, lon, lat, Clicklon, Clicklat);
					},
					error: function (request, status, error) {
							console.log("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
					},
			});
	}
	
    function reset(){
        if(InfoWindow != undefined){
            InfoWindow.setMap(null);
            InfoWindow = undefined;
        }
        if(marker != undefined){
            marker.setMap(null);
        }
        if(rect != undefined){
                rect.setMap(null);
                rect = undefined;
            }
	   }


	function puzzle(url, lon, lat, Clicklon, Clicklat) {
    // 이전 오버레이 삭제
    if (InfoWindow) {
        InfoWindow.setMap(null);
        InfoWindow = undefined;
    }

    $.ajax({
        method: "GET",
        url: url,
        async: false,
        data: {},
        success: function (response) {
            var rltm = response.contents.rltm;
            var congestion, congestionLevel, datetime;
            var congestion2, congestionLevel2, datetime2;

            for (var i = 0; i < rltm.length; i++) {
                if (rltm[i].type == 1) {
                    congestion = (Number(rltm[i].congestion) * 100).toFixed(2);
                    congestionLevel = rltm[i].congestionLevel;
                    datetime = rltm[i].datetime;
                } else if (rltm[i].type == 2) {
                    congestion2 = (Number(rltm[i].congestion) * 100).toFixed(2);
                    congestionLevel2 = rltm[i].congestionLevel;
                    datetime2 = rltm[i].datetime;
                }
            }

            const colorObj = congestionLevelColor(congestionLevel);
            const colorObj2 = congestionLevelColor(congestionLevel2);
            color = colorObj.color;
            congest = colorObj.congest;
            color2 = colorObj2.color;
            congest2 = colorObj2.congest;

            rect = new Tmapv2.Rectangle({
                bounds: new Tmapv2.LatLngBounds(
                    new Tmapv2.LatLng(Number(Clicklat) + 0.0014957, Number(Clicklon) - 0.0018867),
                    new Tmapv2.LatLng(Number(Clicklat) - 0.0014957, Number(Clicklon) + 0.0018867)
                ), // 사각형 영역 좌표
                strokeColor: "#000000", // 테두리 색상
                strokeWeight: 2.5,
                strokeOpacity: 1,
                fillColor: color2, // 사각형 내부 색상
                fillOpacity: 0.5,
                map: map, // 지도 객체
            });

            if (rltm.length >= 2) {
                var year = datetime.substr(0, 4);
                var month = datetime.substr(4, 2);
                var day = datetime.substr(6, 2);
                var hour = datetime.substr(8, 2);
                var min = datetime.substr(10, 2);
                var sec = datetime.substr(12, 2);
                var date = `${year}년 ${month}월 ${day}일 ${hour}시 ${min}분 ${sec}초`;

                var year2 = datetime2.substr(0, 4);
                var month2 = datetime2.substr(4, 2);
                var day2 = datetime2.substr(6, 2);
                var hour2 = datetime2.substr(8, 2);
                var min2 = datetime2.substr(10, 2);
                var sec2 = datetime2.substr(12, 2);
                var date2 = `${year2}년 ${month2}월 ${day2}일 ${hour2}시 ${min2}분 ${sec2}초`;

                result = `[장소] ${name} [${congest}, ${congestion}명/100m²]<br>`;
                result += `[주변] ${name} [${congest2}, ${congestion2}명/100m²]`;

                // 새로운 InfoWindow 생성
                InfoWindow = new Tmapv2.InfoWindow({
                    position: new Tmapv2.LatLng(Clicklat, Clicklon), // 사각형 중심 좌표
                    content: `<div style="background: rgba(255, 255, 255, 0.7); 
                                         border: 1px solid #000; 
                                         padding: 5px; 
                                         border-radius: 5px; 
                                         text-align: center;">
                                 ${result}
                             </div>`, // 텍스트 내용
                    type: 2, // type 2로 설정하면 지도 위 고정
                    map: map, // 지도 객체
                });
            } else {
                result = `[주변] ${name} [${congest2}, ${congestion2}명/100m²]`;

                // 새로운 InfoWindow 생성
                InfoWindow = new Tmapv2.InfoWindow({
                    position: new Tmapv2.LatLng(Clicklat, Clicklon), // 사각형 중심 좌표
                    content: `<div style="background: rgba(255, 255, 255, 0.7); 
                                         border: 1px solid #000; 
                                         padding: 5px; 
                                         border-radius: 5px; 
                                         text-align: center;">
                                 ${result}
                             </div>`, // 텍스트 내용
                    type: 2, // type 2로 설정하면 지도 위 고정
                    map: map, // 지도 객체
                });
            }

        },
        error: function (request, status, error) {
            if (request.status == "404") {
                result = `POI ID: ${poiId}, ${name}, 해당 좌표는 실시간 장소 혼잡도를 지원하고 있지 않습니다.`;
                $("").text(result);
            } else {
                console.log("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
            }
            },
        });
    }
	
    // 혼잡도
	function squareMap() {
    resetActiveStates(); // 다른 기능 초기화
    isSquareMapActive = true; // squareMap 활성화

    $(".api_etc_btns > div#squareMap").addClass("__color_blue_fill");
    $("#map_wrap").html(`
        <div id="map_div" class="map_wrap" style='position: relative; bottom: -20px;'></div>
        <div style='position: relative; bottom: 135px; left: 10px; width: 95px; height: 140px; text-align: center; background: #ffffff; border: 1px solid #808080; border-radius: 3px; font-size: 12px'>
            장소혼잡도 단계
            <div style='width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #9cf7bd; border-radius: 3px; margin: 3px auto'>여유</div>
            <div style='width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #73b7ff; border-radius: 3px; margin: 3px auto'>보통</div>
            <div style='width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #d9a8ed; border-radius: 3px; margin: 3px auto'>혼잡</div>
            <div style='width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #ff96b4; border-radius: 3px; margin: 3px auto'>매우 혼잡</div>
        </div>
    `);
    }
    
    //혼잡도별 색상, 혼잡도 표시 함수
	   function congestionLevelColor(congestionLevel){
		   var congest = ""
		   var color = ""
		   
		   switch(congestionLevel){
			case 1:
				congest ="여유";
				color = '#9cf7bd';
				break;
			case 2:
				congest ="보통";
	  			color ='#73b7ff';
				break;
			case 3:
				congest ="혼잡";
		  		color ='#d9a8ed';
				break;
			case 4:
				congest ="매우 혼잡";
		  		color ='#ff96b4';
				break;
			}
		   return {"color":color,"congest":congest}
	   }

    function resetActiveStates() {
    // 모든 기능의 활성 상태를 초기화
    isSquareMapActive = false;
    isAutoTrafficActive = false;
    isMeasureDistanceActive = false;

    // 버튼 UI 초기화
    $(".api_etc_btns > div").removeClass("__color_blue_fill");
	$(".api_etc_labels > div").hide();

    // 지도 위 객체 초기화
    if (rect) {
        rect.setMap(null);
        rect = undefined;
    }
    if (InfoWindow) {
        InfoWindow.setMap(null);
        InfoWindow = undefined;
    }

		try {
      tData.autoTraffic(map, { trafficOnOff: false });
    } catch (error) {}
    // 지도 초기화
    $("#map_wrap").empty();
    }

    function resetMeasureObject() {
    $(".api_etc_btns > div").removeClass("__color_blue_fill");
    $(".api_etc_labels > div").hide();

    // 기본 정보 제거
    try {
      if (measureDistance) {
        measureDistance.remove();
      }
    } catch (error) {}

    // 교통정보 제거
    try {
      tData.autoTraffic(map, { trafficOnOff: false });
    } catch (error) {}

    // 추가적인 UI 초기화
    $("#map_wrap").empty();
    }
    // puzzle함수 끝

    // 교통정보 시작
    function autoTraffic() {
        resetActiveStates(); // 다른 기능 초기화
        isAutoTrafficActive = true; // autoTraffic 활성화

        $(".api_etc_btns > div#autoTraffic").addClass("__color_blue_fill");
        tData.autoTraffic(map, { trafficOnOff: true });

        $("#map_wrap").html(`
                <div id="map_div" class="map_wrap" style="position: relative; bottom: -20px;"></div>
                <div style="position: relative; bottom: 135px; left: 10px; width: 95px; height: 140px; text-align: center; background: #ffffff; border: 1px solid #808080; border-radius: 3px; font-size: 12px">
                        교통상황 단계
                        <div style="width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #99cc00; border-radius: 3px; margin: 3px auto">여유</div>
                        <div style="width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: yellow; border-radius: 3px; margin: 3px auto">보통</div>
                        <div style="width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: orange; border-radius: 3px; margin: 3px auto">혼잡</div>
                        <div style="width: 84px; height: 25px; border: 1px solid #808080; text-align: center; background: #cc0000; border-radius: 3px; margin: 3px auto">매우 혼잡</div>
                </div>
        `);
	}
	   
	//혼잡도별 색상, 혼잡도 표시 함수
    function congestionLevelColor(congestionLevel){
        var congest = ""
        var color = ""
        
        switch(congestionLevel){
        case 1:
            congest ="여유";
            color = '#9cf7bd';
            break;
        case 2:
            congest ="보통";
            color ='#73b7ff';
            break;
        case 3:
            congest ="혼잡";
            color ='#d9a8ed';
            break;
        case 4:
            congest ="매우 혼잡";
            color ='#ff96b4';
            break;
        }
        return {"color":color,"congest":congest}
    }


    $(document).ready(function() {
        var currentKeyword = $('#searchKeyword').val();
        
        $(".hashtag").hover(
            function() {
                // 마우스가 요소 위에 있을 때
                $(this).css({
                    "background-color": "#FF9E44",
                    "color": "white"
                });
            },
            function() {
                // 마우스가 요소를 벗어났을 때
                if (!$(this).hasClass("active")) {
                    $(this).css({
                        "background-color": "#ffc792",
                        "color": "black"
                    });
                }
            }
        );

        $(".hashtag").on("click", function(e) {
            e.preventDefault(); // 기본 동작 방지
            var text = $(this).text().trim(); // 텍스트 가져오기
            var keyword = text.split('#')[1].trim().slice(0, -2); // # 제거 후 뒤의 단어 추출
            
            // 현재 클릭된 li가 이미 active 상태인지 확인
            if ($(this).hasClass("active")) {
                // active 상태일 경우 비활성화
                $(this).removeClass("active").css({
                    "background-color": "#ffc792",
                    "color": "black"
                });
    
                // 검색창 초기화 및 결과 지우기
                $('#searchKeyword').val("");
                $("#searchResult").html("");
                clearMarkers();
                updateCategoryImage(""); // 모든 li 이미지 상태 초기화
            } else {
                // active 상태가 아닐 경우 활성화
                $(".hashtag").removeClass("active").css({
                    "background-color": "#ffc792",
                    "color": "black"
                });
                $(this).addClass("active").css({
                    "background-color": "#FF9E44",
                    "color": "white"
                });
    
                // 검색창에 키워드 입력
                $("#searchKeyword").val(keyword);
                console.log(keyword);
                $("#btn_select").click(); // 검색 버튼 클릭 트리거 
            }
        });

        // 지도 검색창 기능
        $("#btn_select").on("click", function () {
            var searchKeyword = $('#searchKeyword').val(); // 검색 키워드
            var headers = {};
            headers["appKey"] = "IOWlgu3VCB5vrfwE0YE0w3e24rgK4g612MZZEILt";   
            
            $(".hashtag").each(function() {
                var text = $(this).text().trim();
                var hashtagText = text.split('#')[1].trim().slice(0, -2);
                // 입력된 검색어와 일치하는 해시태그를 활성화
                if (hashtagText === searchKeyword) {
                    $(this).addClass("active").css({
                        "background-color": "#FF9E44",
                        "color": "white"
                    });
                }
            });
            
            // 현재 지도 중심 좌표 가져오기
            var currentCenter, currentLat, currentLon;
            console.log("현재 지도 중심 좌표:", currentLat, currentLon);
            if (map && typeof map.getCenter === 'function') {
            currentCenter = map.getCenter();
            currentLat = currentCenter.lat();
            currentLon = currentCenter.lng();
            } else {
            console.log("map.getCenter() is not available");
            }

            // li 이미지 상태 업데이트
            updateCategoryImage(searchKeyword);
    
            // 카테고리와 관련 없는 키워드 검색 시 10개만 출력, 카테고리 관련 시 50개 출력
            var resultCount = (isCategoryRelated(searchKeyword)) ? 200 : 50;
    
            // 마커 이미지 결정
            var markerImage = getMarkerImage(searchKeyword);
    
            // 검색어가 비어있을 경우 마커와 결과 초기화
            if (!searchKeyword) {
                clearMarkers();  // 마커 및 결과 초기화
                $("#searchResult").html("");  // 검색 결과 목록 초기화
                return;
            }
    
            $.ajax({
                method: "GET", // 요청 방식
                headers: headers,
                url: "https://apis.openapi.sk.com/tmap/pois?version=1&format=json", // url 주소
                data: { // 요청 데이터 정보
                    "searchKeyword": searchKeyword, // 검색 키워드
                    "resCoordType": "EPSG3857", // 응답 좌표계
                    "centerLon": currentLon,
                    "centerLat": currentLat,
                    "count": resultCount // 출력되는 데이터 개수
                },
                success: function (response) {
                    var resultpoisData = response.searchPoiInfo.pois.poi;
    
                    // 기존 마커, 팝업 제거
                    clearMarkers();
    
                    var innerHtml = ""; // searchResult 결과값 노출 위한 변수
                    var positionBounds = new Tmapv2.LatLngBounds(); // LatLngBounds 객체 생성
    
                    // POI 마커 표시
                    for (var k in resultpoisData) {
                        var noorLat = Number(resultpoisData[k].noorLat);
                        var noorLon = Number(resultpoisData[k].noorLon);
                        var name = resultpoisData[k].name;
                        var id = resultpoisData[k].id;
    
                        // 좌표 객체 생성
                        var pointCng = new Tmapv2.Point(noorLon, noorLat);
    
                        // EPSG3857 좌표계를 WGS84GEO 좌표계로 변환
                        var projectionCng = new Tmapv2.Projection.convertEPSG3857ToWGS84GEO(pointCng);
    
                        var lat = projectionCng._lat;
                        var lon = projectionCng._lng;
    
                        var markerPosition = new Tmapv2.LatLng(lat, lon);
    
                        // 마커 설정
                        var marker = new Tmapv2.Marker({
                            position: markerPosition, // 마커 위치
                            icon: markerImage, // 카테고리에 맞는 마커 이미지 사용
                            iconSize: new Tmapv2.Size(30, 35), // 마커 크기 (24x35)
                            title: name, // 마커 제목
                            map: map // 지도에 마커 등록
                        });
    
                        // 결과창에 나타날 HTML 구성
                        innerHtml += "<li><div><img src='" + markerImage + "' style='vertical-align:middle;' class='marker-img'>&nbsp;&nbsp;<span>"
                            + name
                            + "&nbsp;&nbsp;</span><button type='button' name='sendBtn' onClick='poiDetail(" + id + ");'> 상세보기</button></div></li><br>";
    
                        // 마커 배열에 저장
                        markerArr.push(marker);
                        positionBounds.extend(markerPosition); // LatLngBounds 확장
                    }
    
                    // 검색 결과 출력
                    $("#searchResult").html(innerHtml);
    
                    // 바운드 설정 없이, 맵 위치 고정
                    if (markerArr.length > 0) {
                        // 현재 맵의 줌 레벨을 저장
                        var currentZoom = map.getZoom();
    
                        // 마커들이 생성되었을 때만 중심을 설정하고 확대하지 않음
                        var centerPosition = markerArr[0].getPosition(); // 첫 번째 마커 위치로 맵 중심 설정
                        map.setCenter(currentCenter);
    
                        // 기존 줌 레벨을 유지
                        map.setZoom(currentZoom);
                    }
                },
                error: function (request, status, error) {
                    console.log("code:" + request.status + "\n"
                        + "message:" + request.responseText
                        + "\n" + "error:" + error);
                }
            });
        });
        
        
    });
    
    
    // 카테고리 함수 시작
    // 카테고리와 관련된 검색인지 확인하는 함수
    function isCategoryRelated(keyword) {
        var relatedKeywords = ["카페", "ATM", "주차장", "화장실", "약국", "주유소"];  // tmap 카테고리 관련 키워드 목록
        // var angkeywords = ["크리스마스", "와인/바", "비건식당", "연말파티", "브런치", "제철음식", "데이트"];  // 앙꼬 카테고리 관련 키워드 목록
        return relatedKeywords.includes(keyword);
        // return angkeywords.includes(keyword);
    }
    
    // 카테고리에 맞는 마커 이미지 반환 함수
    function getMarkerImage(keyword) {
        // 카테고리 관련 키워드에 맞는 마커 이미지 반환
        if (isCategoryRelated(keyword)) {
            switch (keyword) {
                case "카페":
                    return "/static/images/cafepin.png"; // 카페 마커 이미지
                case "ATM":
                    return "/static/images/atmpin.png"; // ATM 마커 이미지
                case "주차장":
                    return "/static/images/parkpin.png"; // 주차장 마커 이미지
                case "화장실":
                    return "/static/images/bath.png"; // 화장실 마커 이미지
                case "약국":
                    return "/static/images/mad.png"; // 약국 마커 이미지
                case "주유소":
                    return "/static/images/oilpin.png"; // 주유소 마커 이미지
                default:
                    return "/static/images/defaultpin.png"; // 기본 마커 이미지
            }
        } else {
            // 카테고리 관련 없는 경우 기본 마커 이미지
            return "/static/images/default.png"; 
        }
    }
    
    // 카테고리 관련된 li 이미지 업데이트 함수
    function updateCategoryImage(searchKeyword) {
        const listItems = document.querySelectorAll("#s_c li");
    
        listItems.forEach(item => {
            const text = item.textContent.trim(); // li의 텍스트 (카테고리명)
            const imageOff = item.getAttribute("data-image-off");
            const imageOn = item.getAttribute("data-image-on");
    
            if (text === searchKeyword) {
                // 검색어와 일치하는 li를 활성화 상태로 설정
                item.style.backgroundImage = `url(${imageOn})`;
                item.classList.add("active");
            } else {
                // 검색어와 일치하지 않는 li는 비활성화 상태로 설정
                item.style.backgroundImage = `url(${imageOff})`;
                item.classList.remove("active");
            }
        });
    }
    
    // 마커 및 결과 초기화 함수
    function clearMarkers() {
        // 기존 마커, 팝업 제거
        if (markerArr.length > 0) {
            for (var i in markerArr) {
                markerArr[i].setMap(null);
            }
            markerArr = [];
        }
    
        if (labelArr.length > 0) {
            for (var i in labelArr) {
                labelArr[i].setMap(null);
            }
            labelArr = [];
        }
    }
    
    // 카테고리 클릭 이벤트 리스너
    document.addEventListener("DOMContentLoaded", () => {
        const listItems = document.querySelectorAll("#s_c li");
    
        listItems.forEach(item => {
            const imageOff = item.getAttribute("data-image-off");
            item.style.backgroundImage = `url(${imageOff})`;
    
            item.addEventListener("click", () => {
                const searchKeyword = item.textContent.trim();
    
                // 현재 클릭된 카테고리가 이미 활성화 상태일 경우
                if (item.classList.contains("active")) {
                    // 검색창을 초기화하고, 마커와 결과도 초기화
                    $('#searchKeyword').val("");
                    $("#searchResult").html("");
                    clearMarkers();
                    updateCategoryImage(""); // 모든 li 이미지 상태 초기화
                } else {
                    // 모든 li를 초기화
                    listItems.forEach(otherItem => {
                        const otherImageOff = otherItem.getAttribute("data-image-off");
                        otherItem.style.backgroundImage = `url(${otherImageOff})`;
                        otherItem.classList.remove("active"); // 활성화 상태 제거
                    });
    
                    // 클릭한 li를 활성화 상태로 전환
                    const imageOn = item.getAttribute("data-image-on");
                    item.style.backgroundImage = `url(${imageOn})`;
                    item.classList.add("active");
    
                    // 검색창에 입력된 값도 동기화
                    $('#searchKeyword').val(searchKeyword);
    
                    // 검색 결과도 바로 출력
                    $("#btn_select").click();
                }
            });
        });
    });
    // 카테고리 함수 끝


var search_word = $("#searchKeyword").val();
var remote = $("#txt1").val()
console.log("remote :"+remote)
console.log("remote의타입 :"+typeof(remote))
if (remote == "1") {
    console.log("작동중")
    setTimeout(function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var lat = position.coords.latitude;
                var lon = position.coords.longitude;
                setMapCenter(lat, lon, search_word);
            })
        } else {
            console.log("작동실패")
            console.error("Geolocation is not supported by this browser.");
            // 기본 위치 값 사용
            var lat = currentLat;
            var lon = currentLon;
            setMapCenter(lat, lon, search_word);
        }

        updateMapCenter();
        $('#searchKeyword').val(search_word);
        $("#btn_select").trigger('click');

        console.log("Remote:", remote);
        console.log("search_word:", search_word);
    }, 70);  // 딜레이

}

// 4. POI 상세 정보 API
    //--- POI 상세 정보 API Sample >> https://tmapapi.tmapmobility.com/main.html#webservice/sample/WebSamplePoiDetail
    function poiDetail(poiId) {
        var headers = {}; 
        headers["appKey"] = "IOWlgu3VCB5vrfwE0YE0w3e24rgK4g612MZZEILt";
    
        $.ajax({
            method: "GET",
            headers: headers,
            url: "https://apis.openapi.sk.com/tmap/pois/" + poiId + "?version=1&resCoordType=EPSG3857&format=json",
            success: function(response) {
                var detailInfo = response.poiDetailInfo;
                var name = detailInfo.name;
                var telNo = detailInfo.telNo;
                var roadName = detailInfo.roadName;
                var address = detailInfo.address;
                var firstNo = detailInfo.firstNo;
                var secondNo = detailInfo.secondNo;
                var subClassNmC = detailInfo.subClassNmC;
                var desc = detailInfo.desc;
                var id = detailInfo.id;
                var pkey = detailInfo.pkey;
    
                var content = `
                    <div style='position: relative; padding: 20px;'>
                        <div style='position: absolute; top: 10px; right: 10px; cursor: pointer; font-size: 20px;' onclick='closeSlidePanel();'>×</div>
                        <div>
                            <b style='color: black; font-size: 30px; line-height: 1.5;'>${name}</b><br>
                            <b style='color: black; font-size: 30px; line-height: 1.5;'>${id}</b><br>
                            <b style='color: black; font-size: 30px; line-height: 1.5;'>${pkey}</b><br>
                            <b style='font-size: 20px; line-height: 1.5;'>subClassNmC :</b> ${subClassNmC}<br>
                            <b style='font-size: 20px; line-height: 1.5;'><i class="fa-solid fa-location-dot"></i> ${address} ${roadName} ${firstNo}-${secondNo}</b><br>
                            <b style='font-size: 20px; line-height: 1.5;'><i class="fa-solid fa-phone"></i> ${telNo}</b><br>
                            <b style='font-size: 20px; line-height: 1.5; font-weight: 400;'><i class="fa-solid fa-circle-info"></i> ${desc}</b>
                        </div>
                    </div>
                    `;
    
                // 내용 삽입
                document.getElementById("slide_content").innerHTML = content;
    
                // 슬라이드 패널 표시
                var slidePanel = document.getElementById("slide_panel");
                slidePanel.classList.add("active");
            },
            error: function(request, status, error) {
                console.log("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
            }
        });
    }
    
    function closeSlidePanel() {
        var slidePanel = document.getElementById("slide_panel");
        slidePanel.classList.remove("active");
    }


    // 정보 넣기