#!/bin/bash

cd ../policies
yourfilenames=`ls ./*.json`

for eachfile in $yourfilenames
do
    aws accessanalyzer validate-policy --policy-type SERVICE_CONTROL_POLICY --policy-document file://$eachfile > accessanalyzer.out

    if [[ `aws accessanalyzer validate-policy --policy-type SERVICE_CONTROL_POLICY --policy-document file://$eachfile | jq ".findings[].findingDetails" | wc -l` -gt 0 ]]
    then
        echo -e "\nTest failed: IAM Policy $eachfile is invalid\n\n"
        cat accessanalyzer.out
        rm accessanalyzer.out
        exit 1
        
    fi
done