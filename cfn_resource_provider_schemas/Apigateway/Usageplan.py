SCHEMA = {
  "typeName" : "AWS::ApiGateway::UsagePlan",
  "description" : "The ``AWS::ApiGateway::UsagePlan`` resource creates a usage plan for deployed APIs. A usage plan sets a target for the throttling and quota limits on individual client API keys. For more information, see [Creating and Using API Usage Plans in Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) in the *API Gateway Developer Guide*.\n In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using [](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor costs and [](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to manage API requests.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-apigateway.git",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string",
      "description" : ""
    },
    "ApiStages" : {
      "type" : "array",
      "description" : "",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/ApiStage"
      }
    },
    "Description" : {
      "type" : "string",
      "description" : ""
    },
    "Quota" : {
      "$ref" : "#/definitions/QuotaSettings",
      "description" : ""
    },
    "Tags" : {
      "type" : "array",
      "description" : "",
      "insertionOrder" : False,
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Throttle" : {
      "$ref" : "#/definitions/ThrottleSettings",
      "description" : ""
    },
    "UsagePlanName" : {
      "type" : "string",
      "description" : ""
    }
  },
  "definitions" : {
    "ApiStage" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ApiId" : {
          "type" : "string",
          "description" : ""
        },
        "Stage" : {
          "type" : "string",
          "description" : ""
        },
        "Throttle" : {
          "type" : "object",
          "description" : "",
          "additionalProperties" : False,
          "patternProperties" : {
            ".*" : {
              "$ref" : "#/definitions/ThrottleSettings"
            }
          }
        }
      },
      "description" : ""
    },
    "ThrottleSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BurstLimit" : {
          "type" : "integer",
          "minimum" : 0,
          "description" : ""
        },
        "RateLimit" : {
          "type" : "number",
          "minimum" : 0,
          "description" : ""
        }
      },
      "description" : "``ThrottleSettings`` is a property of the [AWS::ApiGateway::UsagePlan](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html) resource that specifies the overall request rate (average requests per second) and burst capacity when users call your REST APIs."
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128,
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -."
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256,
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -."
        }
      },
      "required" : [ "Value", "Key" ],
      "description" : ""
    },
    "QuotaSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Limit" : {
          "type" : "integer",
          "minimum" : 0,
          "description" : ""
        },
        "Offset" : {
          "type" : "integer",
          "minimum" : 0,
          "description" : ""
        },
        "Period" : {
          "type" : "string",
          "description" : ""
        }
      },
      "description" : "``QuotaSettings`` is a property of the [AWS::ApiGateway::UsagePlan](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html) resource that specifies a target for the maximum number of requests users can make to your REST APIs.\n In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using [](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor costs and [](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to manage API requests."
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "apigateway:PUT", "apigateway:DELETE", "apigateway:GET" ]
  },
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "apigateway:POST", "apigateway:GET", "apigateway:PUT" ]
    },
    "read" : {
      "permissions" : [ "apigateway:GET" ]
    },
    "update" : {
      "permissions" : [ "apigateway:GET", "apigateway:DELETE", "apigateway:PATCH", "apigateway:PUT" ]
    },
    "delete" : {
      "permissions" : [ "apigateway:DELETE", "apigateway:GET", "apigateway:PATCH" ]
    },
    "list" : {
      "permissions" : [ "apigateway:GET" ]
    }
  }
}