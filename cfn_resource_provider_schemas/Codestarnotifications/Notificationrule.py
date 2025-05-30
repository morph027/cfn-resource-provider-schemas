SCHEMA = {
  "typeName" : "AWS::CodeStarNotifications::NotificationRule",
  "description" : "Resource Type definition for AWS::CodeStarNotifications::NotificationRule",
  "additionalProperties" : False,
  "properties" : {
    "EventTypeId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "CreatedBy" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "TargetAddress" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "EventTypeIds" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 200
      }
    },
    "Status" : {
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "DetailType" : {
      "type" : "string",
      "enum" : [ "BASIC", "FULL" ]
    },
    "Resource" : {
      "type" : "string",
      "pattern" : "^arn:aws[^:\\s]*:[^:\\s]*:[^:\\s]*:[0-9]{12}:[^\\s]+$"
    },
    "Targets" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Target"
      },
      "maxItems" : 10
    },
    "Tags" : {
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        ".*" : {
          "type" : "string"
        }
      }
    },
    "Name" : {
      "type" : "string",
      "pattern" : "[A-Za-z0-9\\-_ ]+$",
      "minLength" : 1,
      "maxLength" : 64
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:aws[^:\\s]*:codestar-notifications:[^:\\s]+:\\d{12}:notificationrule\\/(.*\\S)?$"
    }
  },
  "definitions" : {
    "Target" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TargetType" : {
          "type" : "string"
        },
        "TargetAddress" : {
          "type" : "string"
        }
      },
      "required" : [ "TargetType", "TargetAddress" ]
    }
  },
  "required" : [ "EventTypeIds", "Resource", "DetailType", "Targets", "Name" ],
  "createOnlyProperties" : [ "/properties/Resource" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/EventTypeId", "/properties/TargetAddress" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "codestar-notifications:createNotificationRule" ]
    },
    "list" : {
      "permissions" : [ "codestar-notifications:listNotificationRules" ]
    },
    "read" : {
      "permissions" : [ "codestar-notifications:describeNotificationRule" ]
    },
    "delete" : {
      "permissions" : [ "codestar-notifications:deleteNotificationRule", "codestar-notifications:describeNotificationRule" ]
    },
    "update" : {
      "permissions" : [ "codestar-notifications:updateNotificationRule", "codestar-notifications:TagResource", "codestar-notifications:UntagResource" ]
    }
  }
}