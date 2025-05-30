SCHEMA = {
  "typeName" : "AWS::MediaPackageV2::OriginEndpointPolicy",
  "description" : "<p>Represents a resource policy that allows or denies access to an origin endpoint.</p>",
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
    "OriginEndpointName" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9_-]+$"
    },
    "Policy" : {
      "type" : [ "object", "string" ]
    }
  },
  "required" : [ "ChannelGroupName", "ChannelName", "OriginEndpointName", "Policy" ],
  "createOnlyProperties" : [ "/properties/ChannelGroupName", "/properties/ChannelName", "/properties/OriginEndpointName" ],
  "primaryIdentifier" : [ "/properties/ChannelGroupName", "/properties/ChannelName", "/properties/OriginEndpointName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "mediapackagev2:GetOriginEndpointPolicy", "mediapackagev2:PutOriginEndpointPolicy" ]
    },
    "read" : {
      "permissions" : [ "mediapackagev2:GetOriginEndpointPolicy" ]
    },
    "update" : {
      "permissions" : [ "mediapackagev2:GetOriginEndpointPolicy", "mediapackagev2:PutOriginEndpointPolicy" ]
    },
    "delete" : {
      "permissions" : [ "mediapackagev2:GetOriginEndpointPolicy", "mediapackagev2:DeleteOriginEndpointPolicy" ]
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