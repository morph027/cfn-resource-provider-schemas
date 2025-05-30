SCHEMA = {
  "typeName" : "AWS::SSMContacts::ContactChannel",
  "description" : "Resource Type definition for AWS::SSMContacts::ContactChannel",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "ContactId" : {
      "description" : "ARN of the contact resource",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048,
      "pattern" : "arn:[-\\w+=\\/,.@]+:[-\\w+=\\/,.@]+:[-\\w+=\\/,.@]*:[0-9]+:([\\w+=\\/,.@:-]+)*"
    },
    "ChannelName" : {
      "description" : "The device name. String of 6 to 50 alphabetical, numeric, dash, and underscore characters.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255,
      "pattern" : "[a-zA-Z 0-9_\\-+'&amp;\\uD83C-\\uDBFF\\uDC00-\\uDFFF\\u2000-\\u3300]+"
    },
    "ChannelType" : {
      "description" : "Device type, which specify notification channel. Currently supported values: “SMS”, “VOICE”, “EMAIL”, “CHATBOT.",
      "type" : "string",
      "enum" : [ "SMS", "VOICE", "EMAIL" ]
    },
    "DeferActivation" : {
      "type" : "boolean",
      "description" : "If you want to activate the channel at a later time, you can choose to defer activation. SSM Incident Manager can't engage your contact channel until it has been activated."
    },
    "ChannelAddress" : {
      "description" : "The details that SSM Incident Manager uses when trying to engage the contact channel.",
      "type" : "string"
    },
    "Arn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the engagement to a contact channel."
    }
  },
  "additionalProperties" : False,
  "oneOf" : [ {
    "required" : [ "ContactId", "ChannelName", "ChannelType", "ChannelAddress" ]
  } ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/ContactId", "/properties/ChannelType" ],
  "writeOnlyProperties" : [ "/properties/DeferActivation" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ssm-contacts:CreateContactChannel", "ssm-contacts:GetContactChannel" ]
    },
    "read" : {
      "permissions" : [ "ssm-contacts:GetContactChannel" ]
    },
    "update" : {
      "permissions" : [ "ssm-contacts:UpdateContactChannel", "ssm-contacts:GetContactChannel" ]
    },
    "delete" : {
      "permissions" : [ "ssm-contacts:DeleteContactChannel", "ssm-contacts:GetContactChannel" ]
    },
    "list" : {
      "permissions" : [ "ssm-contacts:ListContactChannels" ]
    }
  }
}