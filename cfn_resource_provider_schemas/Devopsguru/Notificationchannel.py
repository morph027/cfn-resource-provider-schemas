SCHEMA = {
  "typeName" : "AWS::DevOpsGuru::NotificationChannel",
  "description" : "This resource schema represents the NotificationChannel resource in the Amazon DevOps Guru.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-devops-guru",
  "definitions" : {
    "NotificationChannelConfig" : {
      "description" : "Information about notification channels you have configured with DevOps Guru.",
      "type" : "object",
      "properties" : {
        "Sns" : {
          "$ref" : "#/definitions/SnsChannelConfig"
        },
        "Filters" : {
          "$ref" : "#/definitions/NotificationFilterConfig"
        }
      },
      "additionalProperties" : False
    },
    "SnsChannelConfig" : {
      "description" : "Information about a notification channel configured in DevOps Guru to send notifications when insights are created.",
      "type" : "object",
      "properties" : {
        "TopicArn" : {
          "type" : "string",
          "minLength" : 36,
          "maxLength" : 1024,
          "pattern" : "^arn:aws[a-z0-9-]*:sns:[a-z0-9-]+:\\d{12}:[^:]+$"
        }
      },
      "additionalProperties" : False
    },
    "NotificationFilterConfig" : {
      "description" : "Information about filters of a notification channel configured in DevOpsGuru to filter for insights.",
      "type" : "object",
      "properties" : {
        "Severities" : {
          "$ref" : "#/definitions/InsightSeveritiesFilterList"
        },
        "MessageTypes" : {
          "$ref" : "#/definitions/NotificationMessageTypesFilterList"
        }
      },
      "additionalProperties" : False
    },
    "InsightSeverity" : {
      "description" : "DevOps Guru Insight Severity Enum",
      "type" : "string",
      "enum" : [ "LOW", "MEDIUM", "HIGH" ]
    },
    "NotificationMessageType" : {
      "description" : "DevOps Guru NotificationMessageType Enum",
      "type" : "string",
      "enum" : [ "NEW_INSIGHT", "CLOSED_INSIGHT", "NEW_ASSOCIATION", "SEVERITY_UPGRADED", "NEW_RECOMMENDATION" ]
    },
    "InsightSeveritiesFilterList" : {
      "description" : "DevOps Guru insight severities to filter for",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/InsightSeverity"
      },
      "maxItems" : 3,
      "minItems" : 1
    },
    "NotificationMessageTypesFilterList" : {
      "description" : "DevOps Guru message types to filter for",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/NotificationMessageType"
      },
      "maxItems" : 5,
      "minItems" : 1
    }
  },
  "properties" : {
    "Config" : {
      "$ref" : "#/definitions/NotificationChannelConfig"
    },
    "Id" : {
      "description" : "The ID of a notification channel.",
      "type" : "string",
      "minLength" : 36,
      "maxLength" : 36,
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "Config" ],
  "createOnlyProperties" : [ "/properties/Config" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "devops-guru:AddNotificationChannel", "devops-guru:ListNotificationChannels", "sns:Publish", "sns:GetTopicAttributes", "sns:SetTopicAttributes" ]
    },
    "list" : {
      "permissions" : [ "devops-guru:ListNotificationChannels" ]
    },
    "delete" : {
      "permissions" : [ "devops-guru:RemoveNotificationChannel", "devops-guru:ListNotificationChannels" ]
    },
    "read" : {
      "permissions" : [ "devops-guru:ListNotificationChannels" ]
    }
  }
}