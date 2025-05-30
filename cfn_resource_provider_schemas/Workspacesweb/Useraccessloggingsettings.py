SCHEMA = {
  "typeName" : "AWS::WorkSpacesWeb::UserAccessLoggingSettings",
  "description" : "Definition of AWS::WorkSpacesWeb::UserAccessLoggingSettings Resource Type",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "AssociatedPortalArns" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 2048,
        "minLength" : 20,
        "pattern" : "^arn:[\\w+=\\/,.@-]+:[a-zA-Z0-9\\-]+:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\\/[a-fA-F0-9\\-]{36})+$"
      },
      "insertionOrder" : False
    },
    "KinesisStreamArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "arn:[\\w+=/,.@-]+:kinesis:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:stream/.+",
      "description" : "Kinesis stream ARN to which log events are published."
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 0,
      "insertionOrder" : False
    },
    "UserAccessLoggingSettingsArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[\\w+=\\/,.@-]+:[a-zA-Z0-9\\-]+:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\\/[a-fA-F0-9\\-]{36})+$"
    }
  },
  "required" : [ "KinesisStreamArn" ],
  "readOnlyProperties" : [ "/properties/AssociatedPortalArns", "/properties/UserAccessLoggingSettingsArn" ],
  "primaryIdentifier" : [ "/properties/UserAccessLoggingSettingsArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "workspaces-web:CreateUserAccessLoggingSettings", "workspaces-web:GetUserAccessLoggingSettings", "workspaces-web:ListTagsForResource", "workspaces-web:TagResource" ]
    },
    "read" : {
      "permissions" : [ "workspaces-web:GetUserAccessLoggingSettings", "workspaces-web:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "workspaces-web:UpdateUserAccessLoggingSettings", "workspaces-web:TagResource", "workspaces-web:UntagResource", "workspaces-web:GetUserAccessLoggingSettings", "workspaces-web:ListTagsForResource", "kinesis:PutRecord", "kinesis:PutRecords" ]
    },
    "delete" : {
      "permissions" : [ "workspaces-web:GetUserAccessLoggingSettings", "workspaces-web:DeleteUserAccessLoggingSettings" ]
    },
    "list" : {
      "permissions" : [ "workspaces-web:ListUserAccessLoggingSettings" ]
    }
  },
  "tagging" : {
    "cloudFormationSystemTags" : False,
    "tagOnCreate" : True,
    "tagProperty" : "/properties/Tags",
    "tagUpdatable" : True,
    "taggable" : True,
    "permissions" : [ "workspaces-web:UntagResource", "workspaces-web:ListTagsForResource", "workspaces-web:TagResource" ]
  },
  "additionalProperties" : False
}