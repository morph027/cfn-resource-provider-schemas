SCHEMA = {
  "typeName" : "AWS::SES::ContactList",
  "description" : "Resource schema for AWS::SES::ContactList.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ses.git",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "Topic" : {
      "type" : "object",
      "properties" : {
        "TopicName" : {
          "description" : "The name of the topic.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9_-]{1,64}$"
        },
        "DisplayName" : {
          "description" : "The display name of the topic.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 128
        },
        "Description" : {
          "description" : "The description of the topic.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 500
        },
        "DefaultSubscriptionStatus" : {
          "type" : "string"
        }
      },
      "required" : [ "TopicName", "DisplayName", "DefaultSubscriptionStatus" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ContactListName" : {
      "description" : "The name of the contact list.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]{1,64}$"
    },
    "Description" : {
      "description" : "The description of the contact list.",
      "type" : "string",
      "maxLength" : 500
    },
    "Topics" : {
      "description" : "The topics associated with the contact list.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Topic"
      },
      "minItems" : 0,
      "maxItems" : 20
    },
    "Tags" : {
      "description" : "The tags (keys and values) associated with the contact list.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 0,
      "maxItems" : 50
    }
  },
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/ContactListName" ],
  "primaryIdentifier" : [ "/properties/ContactListName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ses:CreateContactList" ]
    },
    "read" : {
      "permissions" : [ "ses:GetContactList" ]
    },
    "update" : {
      "permissions" : [ "ses:UpdateContactList", "ses:UntagResource", "ses:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "ses:DeleteContactList" ]
    },
    "list" : {
      "permissions" : [ "ses:ListContactLists" ]
    }
  }
}