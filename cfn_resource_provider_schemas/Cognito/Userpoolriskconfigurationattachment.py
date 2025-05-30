SCHEMA = {
  "typeName" : "AWS::Cognito::UserPoolRiskConfigurationAttachment",
  "description" : "Resource Type definition for AWS::Cognito::UserPoolRiskConfigurationAttachment",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "RiskExceptionConfigurationType" : {
      "type" : "object",
      "properties" : {
        "BlockedIPRangeList" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        },
        "SkippedIPRangeList" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        }
      },
      "additionalProperties" : False
    },
    "CompromisedCredentialsActionsType" : {
      "type" : "object",
      "properties" : {
        "EventAction" : {
          "type" : "string"
        }
      },
      "required" : [ "EventAction" ],
      "additionalProperties" : False
    },
    "CompromisedCredentialsRiskConfigurationType" : {
      "type" : "object",
      "properties" : {
        "Actions" : {
          "$ref" : "#/definitions/CompromisedCredentialsActionsType"
        },
        "EventFilter" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        }
      },
      "required" : [ "Actions" ],
      "additionalProperties" : False
    },
    "AccountTakeoverActionType" : {
      "type" : "object",
      "properties" : {
        "EventAction" : {
          "type" : "string"
        },
        "Notify" : {
          "type" : "boolean"
        }
      },
      "required" : [ "EventAction", "Notify" ],
      "additionalProperties" : False
    },
    "AccountTakeoverActionsType" : {
      "type" : "object",
      "properties" : {
        "HighAction" : {
          "$ref" : "#/definitions/AccountTakeoverActionType"
        },
        "LowAction" : {
          "$ref" : "#/definitions/AccountTakeoverActionType"
        },
        "MediumAction" : {
          "$ref" : "#/definitions/AccountTakeoverActionType"
        }
      },
      "additionalProperties" : False
    },
    "NotifyEmailType" : {
      "type" : "object",
      "properties" : {
        "HtmlBody" : {
          "type" : "string"
        },
        "Subject" : {
          "type" : "string"
        },
        "TextBody" : {
          "type" : "string"
        }
      },
      "required" : [ "Subject" ],
      "additionalProperties" : False
    },
    "NotifyConfigurationType" : {
      "type" : "object",
      "properties" : {
        "BlockEmail" : {
          "$ref" : "#/definitions/NotifyEmailType"
        },
        "MfaEmail" : {
          "$ref" : "#/definitions/NotifyEmailType"
        },
        "NoActionEmail" : {
          "$ref" : "#/definitions/NotifyEmailType"
        },
        "From" : {
          "type" : "string"
        },
        "ReplyTo" : {
          "type" : "string"
        },
        "SourceArn" : {
          "type" : "string"
        }
      },
      "required" : [ "SourceArn" ],
      "additionalProperties" : False
    },
    "AccountTakeoverRiskConfigurationType" : {
      "type" : "object",
      "properties" : {
        "Actions" : {
          "$ref" : "#/definitions/AccountTakeoverActionsType"
        },
        "NotifyConfiguration" : {
          "$ref" : "#/definitions/NotifyConfigurationType"
        }
      },
      "required" : [ "Actions" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "UserPoolId" : {
      "type" : "string"
    },
    "ClientId" : {
      "type" : "string"
    },
    "RiskExceptionConfiguration" : {
      "$ref" : "#/definitions/RiskExceptionConfigurationType"
    },
    "CompromisedCredentialsRiskConfiguration" : {
      "$ref" : "#/definitions/CompromisedCredentialsRiskConfigurationType"
    },
    "AccountTakeoverRiskConfiguration" : {
      "$ref" : "#/definitions/AccountTakeoverRiskConfigurationType"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "UserPoolId", "ClientId" ],
  "createOnlyProperties" : [ "/properties/UserPoolId", "/properties/ClientId" ],
  "primaryIdentifier" : [ "/properties/UserPoolId", "/properties/ClientId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "cognito-idp:SetRiskConfiguration", "cognito-idp:DescribeRiskConfiguration", "iam:PassRole" ],
      "timeoutInMinutes" : 2
    },
    "read" : {
      "permissions" : [ "cognito-idp:DescribeRiskConfiguration" ]
    },
    "update" : {
      "permissions" : [ "cognito-idp:SetRiskConfiguration", "cognito-idp:DescribeRiskConfiguration", "iam:PassRole" ],
      "timeoutInMinutes" : 2
    },
    "delete" : {
      "permissions" : [ "cognito-idp:SetRiskConfiguration", "cognito-idp:DescribeRiskConfiguration" ],
      "timeoutInMinutes" : 2
    }
  }
}