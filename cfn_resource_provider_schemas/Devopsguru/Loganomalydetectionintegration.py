SCHEMA = {
  "typeName" : "AWS::DevOpsGuru::LogAnomalyDetectionIntegration",
  "description" : "This resource schema represents the LogAnomalyDetectionIntegration resource in the Amazon DevOps Guru.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "AccountId" : {
      "description" : "User account id, used as the primary identifier for the resource",
      "type" : "string",
      "pattern" : "^\\d{12}$"
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "properties" : {
    "AccountId" : {
      "$ref" : "#/definitions/AccountId"
    }
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/AccountId" ],
  "primaryIdentifier" : [ "/properties/AccountId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "devops-guru:DescribeServiceIntegration", "devops-guru:UpdateServiceIntegration", "logs:TagLogGroup", "logs:UntagLogGroup" ]
    },
    "read" : {
      "permissions" : [ "devops-guru:DescribeServiceIntegration" ]
    },
    "update" : {
      "permissions" : [ "devops-guru:UpdateServiceIntegration", "logs:TagLogGroup", "logs:UntagLogGroup" ]
    },
    "delete" : {
      "permissions" : [ "devops-guru:DescribeServiceIntegration", "devops-guru:UpdateServiceIntegration", "logs:TagLogGroup", "logs:UntagLogGroup" ]
    },
    "list" : {
      "permissions" : [ "devops-guru:DescribeServiceIntegration" ]
    }
  }
}