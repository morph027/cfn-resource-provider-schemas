SCHEMA = {
  "typeName" : "AWS::MediaPackageV2::ChannelPolicy",
  "description" : "<p>Represents a resource-based policy that allows or denies access to a channel.</p>",
  "properties" : {
    "ChannelGroupName" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9_-]+$"
    },
    "ChannelName" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9_-]+$"
    },
    "Policy" : {
      "type" : [ "object", "string" ]
    }
  },
  "required" : [ "ChannelGroupName", "ChannelName", "Policy" ],
  "createOnlyProperties" : [ "/properties/ChannelGroupName", "/properties/ChannelName" ],
  "primaryIdentifier" : [ "/properties/ChannelGroupName", "/properties/ChannelName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "mediapackagev2:GetChannelPolicy", "mediapackagev2:PutChannelPolicy" ]
    },
    "read" : {
      "permissions" : [ "mediapackagev2:GetChannelPolicy" ]
    },
    "update" : {
      "permissions" : [ "mediapackagev2:GetChannelPolicy", "mediapackagev2:PutChannelPolicy" ]
    },
    "delete" : {
      "permissions" : [ "mediapackagev2:GetChannelPolicy", "mediapackagev2:DeleteChannelPolicy" ]
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-mediapackagev2",
  "additionalProperties" : False
}