SCHEMA = {
  "typeName" : "AWS::DataZone::GroupProfile",
  "description" : "Group profiles represent groups of Amazon DataZone users. Groups can be manually created, or mapped to Active Directory groups of enterprise customers. In Amazon DataZone, groups serve two purposes. First, a group can map to a team of users in the organizational chart, and thus reduce the administrative work of a Amazon DataZone project owner when there are new employees joining or leaving a team. Second, corporate administrators use Active Directory groups to manage and update user statuses and so Amazon DataZone domain administrators can use these group memberships to implement Amazon DataZone domain policies.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-datazone",
  "definitions" : {
    "GroupProfileStatus" : {
      "type" : "string",
      "description" : "The status of the group profile.",
      "enum" : [ "ASSIGNED", "NOT_ASSIGNED" ]
    }
  },
  "properties" : {
    "DomainId" : {
      "type" : "string",
      "description" : "The identifier of the Amazon DataZone domain in which the group profile is created.",
      "pattern" : "^dzd[-_][a-zA-Z0-9_-]{1,36}$"
    },
    "DomainIdentifier" : {
      "type" : "string",
      "description" : "The identifier of the Amazon DataZone domain in which the group profile would be created.",
      "pattern" : "^dzd[-_][a-zA-Z0-9_-]{1,36}$"
    },
    "GroupIdentifier" : {
      "type" : "string",
      "description" : "The ID of the group.",
      "pattern" : "(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|[\\p{L}\\p{M}\\p{S}\\p{N}\\p{P}\\t\\n\\r  ]+)"
    },
    "GroupName" : {
      "type" : "string",
      "description" : "The group-name of the Group Profile.",
      "maxLength" : 1024,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z_0-9+=,.@-]+$"
    },
    "Id" : {
      "type" : "string",
      "description" : "The ID of the Amazon DataZone group profile.",
      "pattern" : "^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$"
    },
    "Status" : {
      "$ref" : "#/definitions/GroupProfileStatus"
    }
  },
  "required" : [ "DomainIdentifier", "GroupIdentifier" ],
  "readOnlyProperties" : [ "/properties/DomainId", "/properties/GroupName", "/properties/Id" ],
  "writeOnlyProperties" : [ "/properties/DomainIdentifier", "/properties/GroupIdentifier" ],
  "createOnlyProperties" : [ "/properties/DomainIdentifier", "/properties/GroupIdentifier" ],
  "primaryIdentifier" : [ "/properties/DomainId", "/properties/Id" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "datazone:CreateGroupProfile", "datazone:GetGroupProfile", "datazone:UpdateGroupProfile", "sso:ListProfiles", "sso:GetProfile", "sso:AssociateProfile", "sso:DisassociateProfile" ]
    },
    "read" : {
      "permissions" : [ "datazone:GetGroupProfile" ]
    },
    "update" : {
      "permissions" : [ "datazone:UpdateGroupProfile", "datazone:GetGroupProfile", "sso:ListProfiles", "sso:GetProfile", "sso:AssociateProfile", "sso:DisassociateProfile" ]
    },
    "delete" : {
      "permissions" : [ "datazone:DeleteGroupProfile", "datazone:GetGroupProfile", "datazone:UpdateGroupProfile", "sso:ListProfiles", "sso:GetProfile", "sso:AssociateProfile", "sso:DisassociateProfile" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DomainIdentifier" : {
            "$ref" : "resource-schema.json#/properties/DomainIdentifier"
          }
        },
        "required" : [ "DomainIdentifier" ]
      },
      "permissions" : [ "datazone:SearchGroupProfiles" ]
    }
  },
  "additionalProperties" : False
}