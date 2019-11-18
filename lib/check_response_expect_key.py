# @author : 'CBC'
# @Time   : 2019-11-15
# @File   : check_response_expect_key

import json
from lib.logger import logger
import os

'''接口返回response一定是字典格式的，因为我写的接口测试框架用的orm链接数据库动态从数据库中传参数，
所以返回value可能会不同，但是返回response的key肯定是固定的，所以我这里验证所有的key。

首先遍历expect_response(期望接口返回)，expect_response[n]可能类型字典，列表或者string/int（我
目前没有见过key是int型的），所以使用isinsstance（）去判断value的类型。如果是string就表示是最
简单的一层{key:value}形式，这里就使用has_key来判断response中有没有该key。expect_response[n]
是dict类型，就递归，最后一定会落到string/int类型的分支。如果expect_response[n]是list类型，就
用到enumerate()来拿到索引和值，根据值的类型去判断。
'''


class CheckResponseExpect:
    def check_response_expect_key(self, response, expect_response):
        temp_data = {}
        self.response = response

        for n1 in expect_response:
            print("n1:", n1)

            # 如果值是字典类型
            if isinstance(expect_response[n1], dict):
                print("dict")
                if not CheckResponseExpect.check_response_expect_key(response=response.get(n1), expect_response=expect_response[n1]):
                    # 发邮件
                    # MailFile().checkfail(response=response.get(n1), expect_response=expect_response[n1])
                    return False
                    raise '{},{}'.format(expect_response[n1], response[n1])

            # 如果值是列表类型
            elif isinstance(expect_response[n1], list):
                print("list")
                for expect_index, expect_listValue in enumerate(expect_response[n1]):
                    # print "expect_index:",expect_index
                    # print "expect_listValue:",expect_listValue
                    for response_index, response_listValue in enumerate(response[n1]):
                        # print "response_index:",response_index
                        # print "response_listValue:",response_listValue
                        if isinstance(expect_listValue, dict):
                            CheckResponseExpect.check_response_expect_key(response=response[n1][response_index], expect_response=
                                                                              expect_response[n1][response_index])
                        elif isinstance(expect_listValue, list):
                            if expect_response[n1][expect_index] == response[n1][expect_index]:
                                break
                            else:
                                # MailFile().checkfail(response=response_listValue,expect=expect_listValue)
                                raise Exception("expect_response="+str(expect_response[n1][expect_index])+"\n" +
                                             "response="+str(response[n1][response_index]))
                        else:
                            if expect_response[n1][expect_index] == response[n1][expect_index]:
                                break
                            else:
                                # MailFile().checkfail(response=response[n1][expect_index], expect=expect_response[n1][expect_index])
                                raise Exception("expect_response="+str(expect_listValue)+"\n"+"response="+str(response_listValue))

            else:
                print("string")
                # if response.has_key(n1):
                if n1 in response:
                    if expect_response[n1] == response[n1]:
                        continue
                    else:
                        # logger().info("expect_response中{0}=".format(n1) + str(expect_response.get(n1)) + " <=> " +
                        #              "response中{0}".format(n1) + str(response.get(n1)))
                        print("expect_response中{0} = ".format(n1) + str(expect_response.get(n1)) + " <=> " +
                                     "response中{0} = ".format(n1) + str(response.get(n1)))
                        return False
                else:
                    # temp_data['error_data'] = '{}:{},{}:{}'.format(n1, expect_response[n1], n1, response[n1])
                    # 发送邮件
                    # MailFile().checkfail(response=response[n1], expect=expect_response[n1])
                    # raise Exception("expect_response="+str(expect_response[n1])+"\n"+"response="+str(response.get(n1)))
                    print("expect_response中{0}=".format(n1) + str(expect_response[n1]) + " <=> " + "response中 {0} 不存在".format(n1))
                    return False
        return True


if __name__ == '__main__':
    response = {"msg": "\u6210\u529f", "code": 500}
    expect_response = {"code":"A0000","data":{"banner":{"banner_img_url":"http://ks-festatic-cdn.rightpaddle.net/img-srv/28843b3e-07ad-4e26-a288-99667d889138---banner.gif","banner_redirect_url":"http://qa.rightpaddle.com/growth_invite/"},"jobs":{"jobs_list":[{"current_timestamp":1573805770,"disable":0,"params":{"reward_amount":100,"reward_type":4,"reward_type_desc":"金币","task_id":708,"task_state":1,"task_type":1},"show_gold_amount":100,"start_time":1567577645,"type":1},{"current_timestamp":1573805770,"disable":0,"params":{"reward_amount":100,"reward_type":4,"reward_type_desc":"金币","task_id":709,"task_state":1,"task_type":2},"show_gold_amount":100,"start_time":1567577645,"type":2}]},"my_gain":{"today_gain":0,"total_gain":1916,"total_gain_rmb":"0.19","week_gain":0},"pkg_type":2,"sign":{"all_sign_days":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],"sign_amount":[288,320,360,388,400,400,5000,466,488,500,500,520,588,600,10000,666,666,700,750,770,800,820,888,888,900,920,950,999,999,20000],"signed_days":[],"today_is_signed":0}},"msg":""}
    check_Response_Expect = CheckResponseExpect()
    if check_Response_Expect.check_response_expect_key(response, expect_response):
        print("返回结果相同")
    else:
        print("结果异常")