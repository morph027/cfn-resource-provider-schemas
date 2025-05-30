SCHEMA = {
  "typeName" : "AWS::SES::MailManagerAddonSubscription",
  "description" : "Definition of AWS::SES::MailManagerAddonSubscription Resource Type",
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
    "AddonName" : {
      "type" : "string"
    },
    "AddonSubscriptionArn" : {
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
  "required" : [ "AddonName" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ses:TagResource", "ses:UntagResource" ]
  },
  "createOnlyProperties" : [ "/properties/AddonName" ],
  "readOnlyProperties" : [ "/properties/AddonSubscriptionArn", "/properties/AddonSubscriptionId" ],
  "primaryIdentifier" : [ "/properties/AddonSubscriptionId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ses:TagResource", "ses:ListTagsForResource", "ses:GetAddonSubscription", "ses:CreateAddonSubscription" ]
    },
    "read" : {
      "permissions" : [ "ses:ListTagsForResource", "ses:GetAddonSubscription" ]
    },
    "update" : {
      "permissions" : [ "ses:TagResource", "ses:UntagResource", "ses:ListTagsForResource", "ses:GetAddonSubscription" ]
    },
    "delete" : {
      "permissions" : [ "ses:GetAddonSubscription", "ses:DeleteAddonSubscription" ]
    },
    "list" : {
      "permissions" : [ "ses:ListAddonSubscriptions" ]
    }
  },
  "additionalProperties" : False
}