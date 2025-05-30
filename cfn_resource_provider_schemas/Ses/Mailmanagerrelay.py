SCHEMA = {
  "typeName" : "AWS::SES::MailManagerRelay",
  "description" : "Definition of AWS::SES::MailManagerRelay Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ses-mailmanager",
  "definitions" : {
    "NoAuthentication" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "RelayAuthentication" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "SecretArn",
        "properties" : {
          "SecretArn" : {
            "type" : "string",
            "pattern" : "^arn:(aws|aws-cn|aws-us-gov):secretsmanager:[a-z0-9-]+:\\d{12}:secret:[a-zA-Z0-9/_+=,.@-]+$"
          }
        },
        "required" : [ "SecretArn" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "NoAuthentication",
        "properties" : {
          "NoAuthentication" : {
            "$ref" : "#/definitions/NoAuthentication"
          }
        },
        "required" : [ "NoAuthentication" ],
        "additionalProperties" : False
      } ]
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z0-9/_\\+=\\.:@\\-]+$"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "pattern" : "^[a-zA-Z0-9/_\\+=\\.:@\\-]*$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ses:TagResource", "ses:UntagResource" ]
  },
  "properties" : {
    "Authentication" : {
      "$ref" : "#/definitions/RelayAuthentication"
    },
    "RelayArn" : {
      "type" : "string"
    },
    "RelayId" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9-]+$"
    },
    "RelayName" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9-_]+$"
    },
    "ServerName" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9-\\.]+$"
    },
    "ServerPort" : {
      "type" : "number",
      "maximum" : 65535,
      "minimum" : 1
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 0
    }
  },
  "required" : [ "Authentication", "ServerName", "ServerPort" ],
  "readOnlyProperties" : [ "/properties/RelayArn", "/properties/RelayId" ],
  "primaryIdentifier" : [ "/properties/RelayId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ses:TagResource", "ses:ListTagsForResource", "ses:GetRelay", "ses:CreateRelay" ]
    },
    "read" : {
      "permissions" : [ "ses:ListTagsForResource", "ses:GetRelay" ]
    },
    "update" : {
      "permissions" : [ "ses:TagResource", "ses:UntagResource", "ses:ListTagsForResource", "ses:GetRelay", "ses:UpdateRelay" ]
    },
    "delete" : {
      "permissions" : [ "ses:GetRelay", "ses:DeleteRelay" ]
    },
    "list" : {
      "permissions" : [ "ses:ListRelays" ]
    }
  },
  "additionalProperties" : False
}