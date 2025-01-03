from django.shortcuts import render
from pros.models import adminUser
from django.http import JsonResponse
# from django.contrib.auth.hashers import check_password  # 암호화 된 비밀번호와 원래 비밀번호 비교

# 관리자 로그인 페이지
def prologin(request):
        return render(request, 'login2.html')
# 관리자 로그인
def prologinChk(request):
    id = request.POST.get("id", "")
    pw = request.POST.get("pw", "")
    qs = adminUser.objects.filter(id=id, pw=pw).first()
    if qs:
        request.session["session_adminId"] = qs.id
        request.session["session_adminName"] = qs.name
        context = {"result": "success"}
    else:
        context = {"result": "fail"}
    return JsonResponse(context)

    # 추후 암호화 예정
    # db에서 해당 아이디 검색
    # try:
    #     adminUser = adminUser.objects.get(id=id)
    #     # 입력된 비밀번호와 저장된 암호화된 비밀번호 비교
    #     if check_password(pw, adminUser.pw):
    #         # 로그인 성공, 세션에 사용자 정보 저장
    #         request.session["session_id"] = adminUser.id
    #         request.session["session_nickname"] = adminUser.nickname
    #         list_qs = list(adminUser.objects.filter(id=id).values())  # 사용자 정보 가져오기
    #         context = {"result": "success", "member": list_qs}  # member 정보를 JSON으로 반환
    #     else:
    #         context = {"result": "fail", "message": "비밀번호가 틀렸습니다."}
    # except adminUser.DoesNotExist:
    #     context = {"result": "fail", "message": "아이디가 존재하지 않습니다."}

# 관리자 페이지 접근
def prolayout(request):
    return render(request, 'pros_layout-static.html')