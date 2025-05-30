SCHEMA = {
  "typeName" : "AWS::MediaLive::CloudWatchAlarmTemplateGroup",
  "description" : "Definition of AWS::MediaLive::CloudWatchAlarmTemplateGroup Resource Type",
  "definitions" : {
    "TagMap" : {
      "type" : "object",
      "description" : "Represents the tags associated with a resource.",
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:.+:medialive:.+:cloudwatch-alarm-template-group:.+$",
      "description" : "A cloudwatch alarm template group's ARN (Amazon Resource Name)"
    },
    "CreatedAt" : {
      "type" : "string",
      "format" : "date-time"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 0,
      "description" : "A resource's optional description."
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 11,
      "minLength" : 7,
      "pattern" : "^(aws-)?[0-9]{7}$",
      "description" : "A cloudwatch alarm template group's id. AWS provided template groups have ids that start with `aws-`"
    },
    "Identifier" : {
      "type" : "string"
    },
    "ModifiedAt" : {
      "type" : "string",
      "format" : "date-time"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^[^\\s]+$",
      "description" : "A resource's name. Names must be unique within the scope of a resource type in a specific region."
    },
    "Tags" : {
      "$ref" : "#/definitions/TagMap"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "medialive:CreateTags", "medialive:DeleteTags" ]
  },
  "required" : [ "Name" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/Id", "/properties/Identifier", "/properties/ModifiedAt" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/Identifier" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "medialive:CreateCloudWatchAlarmTemplateGroup", "medialive:GetCloudWatchAlarmTemplateGroup", "medialive:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "medialive:GetCloudWatchAlarmTemplateGroup" ]
    },
    "update" : {
      "permissions" : [ "medialive:UpdateCloudWatchAlarmTemplateGroup", "medialive:GetCloudWatchAlarmTemplateGroup", "medialive:CreateTags", "medialive:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "medialive:DeleteCloudWatchAlarmTemplateGroup" ]
    },
    "list" : {
      "permissions" : [ "medialive:ListCloudWatchAlarmTemplateGroups" ]
    }
  },
  "additionalProperties" : False
}