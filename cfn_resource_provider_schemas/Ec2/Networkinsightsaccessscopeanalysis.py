SCHEMA = {
  "typeName" : "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
  "description" : "Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2-ni.git",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Key" ]
    }
  },
  "properties" : {
    "NetworkInsightsAccessScopeAnalysisId" : {
      "type" : "string"
    },
    "NetworkInsightsAccessScopeAnalysisArn" : {
      "type" : "string"
    },
    "NetworkInsightsAccessScopeId" : {
      "type" : "string"
    },
    "Status" : {
      "type" : "string",
      "enum" : [ "running", "failed", "succeeded" ]
    },
    "StatusMessage" : {
      "type" : "string"
    },
    "StartDate" : {
      "type" : "string"
    },
    "EndDate" : {
      "type" : "string"
    },
    "FindingsFound" : {
      "type" : "string",
      "enum" : [ "True", "False", "unknown" ]
    },
    "AnalyzedEniCount" : {
      "type" : "integer"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:CreateTags", "ec2:DeleteTags" ]
  },
  "required" : [ "NetworkInsightsAccessScopeId" ],
  "readOnlyProperties" : [ "/properties/NetworkInsightsAccessScopeAnalysisId", "/properties/NetworkInsightsAccessScopeAnalysisArn", "/properties/Status", "/properties/StatusMessage", "/properties/StartDate", "/properties/EndDate", "/properties/FindingsFound", "/properties/AnalyzedEniCount" ],
  "createOnlyProperties" : [ "/properties/NetworkInsightsAccessScopeId" ],
  "primaryIdentifier" : [ "/properties/NetworkInsightsAccessScopeAnalysisId" ],
  "additionalIdentifiers" : [ [ "/properties/NetworkInsightsAccessScopeAnalysisArn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateTags", "ec2:StartNetworkInsightsAccessScopeAnalysis", "ec2:GetTransitGatewayRouteTablePropagations", "ec2:Describe*", "elasticloadbalancing:Describe*", "directconnect:Describe*", "tiros:CreateQuery", "tiros:GetQueryAnswer", "tiros:GetQueryExplanation" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeNetworkInsightsAccessScopeAnalyses" ]
    },
    "update" : {
      "permissions" : [ "ec2:DescribeNetworkInsightsAccessScopeAnalyses", "ec2:CreateTags", "ec2:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteNetworkInsightsAccessScopeAnalysis", "ec2:DeleteTags" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeNetworkInsightsAccessScopeAnalyses" ]
    }
  }
}