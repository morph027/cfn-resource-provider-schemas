SCHEMA = {
  "typeName" : "AWS::XRay::TransactionSearchConfig",
  "description" : "This schema provides construct and validation rules for AWS-XRay TransactionSearchConfig resource parameters.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "AccountId" : {
      "$ref" : "#/definitions/AccountId"
    },
    "IndexingPercentage" : {
      "$ref" : "#/definitions/IndexingPercentage"
    }
  },
  "definitions" : {
    "AccountId" : {
      "description" : "User account id, used as the primary identifier for the resource",
      "type" : "string",
      "pattern" : "^\\d{12}$"
    },
    "IndexingPercentage" : {
      "description" : "Determines the percentage of traces indexed from CloudWatch Logs to X-Ray",
      "type" : "number",
      "minimum" : 0,
      "maximum" : 100
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "application-signals:StartDiscovery", "iam:CreateServiceLinkedRole", "logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutRetentionPolicy", "xray:GetIndexingRules", "xray:GetTraceSegmentDestination", "xray:UpdateIndexingRule", "xray:UpdateTraceSegmentDestination" ]
    },
    "read" : {
      "permissions" : [ "xray:GetTraceSegmentDestination", "xray:GetIndexingRules" ]
    },
    "list" : {
      "permissions" : [ "xray:GetTraceSegmentDestination", "xray:GetIndexingRules" ]
    },
    "update" : {
      "permissions" : [ "xray:GetIndexingRules", "xray:GetTraceSegmentDestination", "xray:UpdateIndexingRule" ]
    },
    "delete" : {
      "permissions" : [ "xray:GetTraceSegmentDestination", "xray:UpdateTraceSegmentDestination", "xray:UpdateIndexingRule" ]
    }
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/AccountId" ],
  "primaryIdentifier" : [ "/properties/AccountId" ]
}