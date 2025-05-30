SCHEMA = {
  "typeName" : "AWS::XRay::Group",
  "description" : "This schema provides construct and validation rules for AWS-XRay Group resource parameters.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "FilterExpression" : {
      "description" : "The filter expression defining criteria by which to group traces.",
      "type" : "string"
    },
    "GroupName" : {
      "description" : "The case-sensitive name of the new group. Names must be unique.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 32
    },
    "GroupARN" : {
      "description" : "The ARN of the group that was generated on creation.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 400
    },
    "InsightsConfiguration" : {
      "$ref" : "#/definitions/InsightsConfiguration"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "definitions" : {
    "InsightsConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InsightsEnabled" : {
          "description" : "Set the InsightsEnabled value to True to enable insights or False to disable insights.",
          "type" : "boolean"
        },
        "NotificationsEnabled" : {
          "description" : "Set the NotificationsEnabled value to True to enable insights notifications. Notifications can only be enabled on a group with InsightsEnabled set to true.",
          "type" : "boolean"
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag."
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag."
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "GroupName" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "xray:TagResource", "xray:UntagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "xray:CreateGroup", "xray:TagResource" ]
    },
    "read" : {
      "permissions" : [ "xray:GetGroup", "xray:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "xray:UpdateGroup", "xray:TagResource", "xray:UntagResource", "xray:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "xray:DeleteGroup" ]
    },
    "list" : {
      "permissions" : [ "xray:GetGroups", "xray:ListTagsForResource" ]
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/GroupARN" ],
  "readOnlyProperties" : [ "/properties/GroupARN" ]
}