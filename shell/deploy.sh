#!/bin/bash

#版本环境
APIENV=${env}
#分支版本
BRANCH=${branch}
#构建目录
DIR_HOME=/tmp/20200427151802

rm -rf ${DIR_HOME}
mkdir -p ${DIR_HOME}

echo "******************env=${env},branch=${branch}**********************************************************************"

cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建h3-pom---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-base/h3-pom.git
cd ${DIR_HOME}/h3-pom
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q  -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi


cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建h3-common---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/common.git
cd ${DIR_HOME}/common
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q  -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi


cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建h3-hdframe---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-base/h3-hdframe.git
cd ${DIR_HOME}/h3-hdframe
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q  -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi

cd ${DIR_HOME}
echo "###################################################################################################################"
echo "供应商中心h3-internal-api-supplier---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-supplier.git
cd ${DIR_HOME}/h3-supplier/h3-internal-api-supplier
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi

cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建价格h3-price-api---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-price.git
cd ${DIR_HOME}/h3-price/h3-internal-api-price
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q  -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi


cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建顾客会员h3-customer-api---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-customer.git
cd ${DIR_HOME}/h3-customer/h3-internal-api-customer
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q  -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi


cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建商品h3-internal-api-ware---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-ware.git
cd ${DIR_HOME}/h3-ware/h3-internal-api-ware
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi

cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建门店信息h3-internal-api-store---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-store.git
cd ${DIR_HOME}/h3-store/h3-internal-api-store
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi


cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建财务中心h3-internal-api-finance---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-finance.git
cd ${DIR_HOME}/h3-finance/h3-internal-api-finance
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi

cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建采购中心h3-internal-api-purchase---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-purchase.git
cd ${DIR_HOME}/h3-purchase/h3-internal-api-purchase
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi


cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建库存中心h3-internal-api-stock---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-stock.git
cd ${DIR_HOME}/h3-stock/h3-internal-api-stock
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi



cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建交易中心h3-internal-api-trade---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-trade.git
cd ${DIR_HOME}/h3-trade/h3-internal-api-trade
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi


cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建仓储中心h3-internal-api-warehouse---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-warehouse.git
cd ${DIR_HOME}/h3-warehouse/h3-internal-api-warehouse
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi




cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建组织架构中心h3-internal-api-organization---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-orgmanager.git
cd ${DIR_HOME}/h3-orgmanager/h3-internal-api-organization
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi


cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建支付中心h3-internal-api-pay---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-pay.git
cd ${DIR_HOME}/h3-pay/h3-internal-api-pay
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi

cd ${DIR_HOME}
echo "###################################################################################################################"
echo "构建档案中心h3-internal-api-basic-setting---------- >>>>>>>>>>>>"
git clone -b ${BRANCH} http://h3-jenkins:5qLoP4yxLcVYNqECRcSl@222.244.144.163:5299/h3-business/h3-basic-setting.git
cd ${DIR_HOME}/h3-basic-setting/h3-internal-api-basic-setting
branch=$(git branch | grep $BRANCH)
if [ -n "$branch" ]; then
    mvn clean deploy -q -Dapi.env=$APIENV -Dmaven.test.skip=true
    if [ $? -ne 0 ]; then
	    echo "FAILED"
	else
	    echo "SUCCEED"
	fi
else
    echo "$BRANCH not exist"
fi




