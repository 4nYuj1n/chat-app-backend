from db.identity_key import select_identity_key
from db.curve_key import select_curve_key
from db.user import select_user
from db.one_time_pqkem import count_one_time_pqkem,select_one_time_pqkem
from db.last_resort_pqkem import select_last_resort_pqkem
from db.one_time_curve_key import count_one_time_curve_key,select_one_time_curve_key
def get_key_bundle(request,username:str):
    try:
        uid = select_user(username)[0]
        IK = select_identity_key(uid)[0][1]
        _,SPK,ISPK,SigSPK,_ = select_curve_key(uid)[0]
        if int(count_one_time_pqkem(uid)[0])>0:
            _,_,PQK,IPQK,SigPQK,_ = select_one_time_pqkem(uid)
        else:
            _,PQK,IPQK,SigPQK,_  = select_last_resort_pqkem(uid)
        if int(count_one_time_curve_key(uid)[0])>0:
            _,_,OPK,IOPK,_ = select_one_time_curve_key(uid)[0]
            return {
                "code" : "200",
                "status" : "success",
                "message" : {
                    "IK" : IK,
                    "SPK" : SPK,
                    "ISPK" : ISPK,
                    "SigSPK" : SigSPK,
                    "PQK" : PQK,
                    "IPQK" : IPQK,
                    "SigPQK" : SigPQK,
                    "OPK" : OPK,
                    "IOPK" : IOPK
                }
            }
        else:
            return {
                "code" : "200",
                "status" : "success",
                "message" : {
                    "IK" : IK,
                    "SPK" : SPK,
                    "ISPK" : ISPK,
                    "SigSPK" : SigSPK,
                    "PQK" : PQK,
                    "IPQK" : IPQK,
                    "SigPQK" : SigPQK,
                }
            }
    except:
        return{
            "code" : "500",
            "status" : "failed",
            "message" : "user not found"
        }
    
        
    