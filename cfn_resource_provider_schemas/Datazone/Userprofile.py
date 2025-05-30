SCHEMA = {
  "typeName" : "AWS::DataZone::UserProfile",
  "description" : "A user profile represents Amazon DataZone users. Amazon DataZone supports both IAM roles and SSO identities to interact with the Amazon DataZone Management Console and the data portal for different purposes. Domain administrators use IAM roles to perform the initial administrative domain-related work in the Amazon DataZone Management Console, including creating new Amazon DataZone domains, configuring metadata form types, and implementing policies. Data workers use their SSO corporate identities via Identity Center to log into the Amazon DataZone Data Portal and access projects where they have memberships.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-datazone",
  "definitions" : {
    "IamUserProfileDetails" : {
      "type" : "object",
      "description" : "The details of the IAM User Profile.",
      "properties" : {
        "Arn" : {
          "type" : "string",
          "description" : "The ARN of the IAM User Profile."
        }
      },
      "additionalProperties" : False
    },
    "SsoUserProfileDetails" : {
      "type" : "object",
      "description" : "The details of the SSO User Profile.",
      "properties" : {
        "Username" : {
          "type" : "string",
          "description" : "The username of the SSO User Profile.",
          "maxLength" : 1024,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z_0-9+=,.@-]+$"
        },
        "FirstName" : {
          "type" : "string",
          "description" : "The First Name of the IAM User Profile."
        },
        "LastName" : {
          "type" : "string",
          "description" : "The Last Name of the IAM User Profile."
        }
      },
      "additionalProperties" : False
    },
    "UserProfileDetails" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "Iam",
        "properties" : {
          "Iam" : {
            "$ref" : "#/definitions/IamUserProfileDetails"
          }
        },
        "required" : [ "Iam" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "Sso",
        "properties" : {
          "Sso" : {
            "$ref" : "#/definitions/SsoUserProfileDetails"
          }
        },
        "required" : [ "Sso" ],
        "additionalProperties" : False
      } ]
    },
    "UserProfileStatus" : {
      "type" : "string",
      "description" : "The status of the user profile.",
      "enum" : [ "ASSIGNED", "NOT_ASSIGNED", "ACTIVATED", "DEACTIVATED" ]
    },
    "UserProfileType" : {
      "type" : "string",
      "description" : "The type of the user profile.",
      "enum" : [ "IAM", "SSO" ]
    },
    "UserType" : {
      "type" : "string",
      "description" : "The type of the user.",
      "enum" : [ "IAM_USER", "IAM_ROLE", "SSO_USER" ]
    }
  },
  "properties" : {
    "Details" : {
      "$ref" : "#/definitions/UserProfileDetails"
    },
    "DomainId" : {
      "type" : "string",
      "description" : "The identifier of the Amazon DataZone domain in which the user profile is created.",
      "pattern" : "^dzd[-_][a-zA-Z0-9_-]{1,36}$"
    },
    "DomainIdentifier" : {
      "type" : "string",
      "description" : "The identifier of the Amazon DataZone domain in which the user profile would be created.",
      "pattern" : "^dzd[-_][a-zA-Z0-9_-]{1,36}$"
    },
    "Id" : {
      "type" : "string",
      "description" : "The ID of the Amazon DataZone user profile."
    },
    "Status" : {
      "$ref" : "#/definitions/UserProfileStatus"
    },
    "Type" : {
      "$ref" : "#/definitions/UserProfileType"
    },
    "UserIdentifier" : {
      "type" : "string",
      "description" : "The ID of the user.",
      "pattern" : "(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|^[a-zA-Z_0-9+=,.@-]+$|^arn:aws:iam::\\d{12}:.+$)"
    },
    "UserType" : {
      "$ref" : "#/definitions/UserType"
    }
  },
  "required" : [ "DomainIdentifier", "UserIdentifier" ],
  "readOnlyProperties" : [ "/properties/DomainId", "/properties/Type", "/properties/Id", "/properties/Details" ],
  "writeOnlyProperties" : [ "/properties/DomainIdentifier", "/properties/UserIdentifier", "/properties/UserType" ],
  "createOnlyProperties" : [ "/properties/DomainIdentifier", "/properties/UserIdentifier", "/properties/UserType" ],
  "primaryIdentifier" : [ "/properties/DomainId", "/properties/Id" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "datazone:CreateUserProfile", "datazone:GetUserProfile", "datazone:UpdateUserProfile", "datazone:GetDomain", "sso:ListProfiles", "sso:GetProfile", "sso:AssociateProfile", "sso:DisassociateProfile", "iam:GetRole", "iam:GetUser" ]
    },
    "read" : {
      "permissions" : [ "datazone:GetUserProfile" ]
    },
    "update" : {
      "permissions" : [ "datazone:UpdateUserProfile", "datazone:GetUserProfile", "datazone:UpdateUserProfile", "sso:ListProfiles", "sso:GetProfile", "sso:AssociateProfile", "sso:DisassociateProfile", "iam:GetRole", "iam:GetUser" ]
    },
    "delete" : {
      "permissions" : [ "datazone:DeleteUserProfile", "datazone:GetUserProfile", "datazone:UpdateUserProfile", "sso:ListProfiles", "sso:GetProfile", "sso:AssociateProfile", "sso:DisassociateProfile", "iam:GetRole", "iam:GetUser" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DomainIdentifier" : {
            "$ref" : "resource-schema.json#/properties/DomainIdentifier"
          },
          "UserType" : {
            "$ref" : "resource-schema.json#/properties/UserType"
          }
        },
        "required" : [ "DomainIdentifier", "UserType" ]
      },
      "permissions" : [ "datazone:SearchUserProfiles" ]
    }
  },
  "additionalProperties" : False
}