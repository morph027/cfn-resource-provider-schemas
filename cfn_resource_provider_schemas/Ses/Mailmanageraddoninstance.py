SCHEMA = {
  "typeName" : "AWS::SES::MailManagerAddonInstance",
  "description" : "Definition of AWS::SES::MailManagerAddonInstance Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ses-mailmanager",
  "definitions" : {
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
  "properties" : {
    "AddonInstanceArn" : {
      "type" : "string"
    },
    "AddonInstanceId" : {
      "type" : "string",
      "maxLength" : 67,
      "minLength" : 4,
      "pattern" : "^ai-[a-zA-Z0-9]{1,64}$"
    },
    "AddonName" : {
      "type" : "string"
    },
    "AddonSubscriptionId" : {
      "type" : "string",
      "maxLength" : 67,
      "minLength" : 4,
      "pattern" : "^as-[a-zA-Z0-9]{1,64}$"
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
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ses:TagResource", "ses:UntagResource" ]
  },
  "required" : [ "AddonSubscriptionId" ],
  "readOnlyProperties" : [ "/properties/AddonInstanceArn", "/properties/AddonInstanceId", "/properties/AddonName" ],
  "createOnlyProperties" : [ "/properties/AddonSubscriptionId" ],
  "primaryIdentifier" : [ "/properties/AddonInstanceId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ses:TagResource", "ses:ListTagsForResource", "ses:GetAddonInstance", "ses:CreateAddonInstance" ]
    },
    "read" : {
      "permissions" : [ "ses:ListTagsForResource", "ses:GetAddonInstance" ]
    },
    "update" : {
      "permissions" : [ "ses:TagResource", "ses:UntagResource", "ses:ListTagsForResource", "ses:GetAddonInstance" ]
    },
    "delete" : {
      "permissions" : [ "ses:GetAddonInstance", "ses:DeleteAddonInstance" ]
    },
    "list" : {
      "permissions" : [ "ses:ListAddonInstances" ]
    }
  },
  "additionalProperties" : False
}