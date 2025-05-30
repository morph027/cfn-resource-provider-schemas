SCHEMA = {
  "typeName" : "AWS::SES::MailManagerAddressList",
  "description" : "Definition of AWS::SES::MailManagerAddressList Resource Type",
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
    "AddressListArn" : {
      "type" : "string"
    },
    "AddressListId" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9-]+$"
    },
    "AddressListName" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9_.-]+$"
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
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/AddressListId" ],
  "readOnlyProperties" : [ "/properties/AddressListId", "/properties/AddressListArn" ],
  "createOnlyProperties" : [ "/properties/AddressListName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ses:TagResource", "ses:ListTagsForResource", "ses:GetAddressList", "ses:CreateAddressList" ]
    },
    "read" : {
      "permissions" : [ "ses:ListTagsForResource", "ses:GetAddressList" ]
    },
    "delete" : {
      "permissions" : [ "ses:GetAddressList", "ses:DeleteAddressList" ]
    },
    "update" : {
      "permissions" : [ "ses:TagResource", "ses:UntagResource", "ses:ListTagsForResource", "ses:GetAddressList" ]
    },
    "list" : {
      "permissions" : [ "ses:ListAddressLists" ]
    }
  }
}