SCHEMA = {
  "typeName" : "AWS::MediaTailor::ChannelPolicy",
  "description" : "Definition of AWS::MediaTailor::ChannelPolicy Resource Type",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "properties" : {
    "ChannelName" : {
      "type" : "string"
    },
    "Policy" : {
      "type" : [ "object", "string" ],
      "description" : "<p>The IAM policy for the channel. IAM policies are used to control access to your channel.</p>"
    }
  },
  "createOnlyProperties" : [ "/properties/ChannelName" ],
  "primaryIdentifier" : [ "/properties/ChannelName" ],
  "required" : [ "ChannelName", "Policy" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "mediatailor:PutChannelPolicy", "mediatailor:GetChannelPolicy" ]
    },
    "read" : {
      "permissions" : [ "mediatailor:GetChannelPolicy" ]
    },
    "update" : {
      "permissions" : [ "mediatailor:PutChannelPolicy", "mediatailor:GetChannelPolicy" ]
    },
    "delete" : {
      "permissions" : [ "mediatailor:DeleteChannelPolicy", "mediatailor:GetChannelPolicy" ]
    }
  },
  "additionalProperties" : False
}