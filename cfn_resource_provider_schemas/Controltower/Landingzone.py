SCHEMA = {
  "tagging" : {
    "permissions" : [ "controltower:UntagResource", "controltower:TagResource", "controltower:ListTagsForResource" ],
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : True
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "controltower:GetLandingZone", "controltower:ListTagsForResource" ]
    },
    "create" : {
      "permissions" : [ "controltower:CreateLandingZone", "controltower:GetLandingZoneOperation", "controltower:ListTagsForResource", "controltower:TagResource", "controltower:GetLandingZone", "cloudformation:DescribeOrganizationsAccess", "servicecatalog:AssociatePrincipalWithPortfolio", "servicecatalog:AssociateProductWithPortfolio", "servicecatalog:CreatePortfolio", "servicecatalog:CreateProduct", "servicecatalog:CreateProvisioningArtifact", "servicecatalog:ListPortfolios", "servicecatalog:ListProvisioningArtifacts", "servicecatalog:SearchProductsAsAdmin", "servicecatalog:UpdatePortfolio", "servicecatalog:UpdateProvisioningArtifact", "servicecatalog:ListPrincipalsForPortfolio", "organizations:CreateOrganizationalUnit", "organizations:CreateOrganization", "organizations:UpdatePolicy", "organizations:CreatePolicy", "organizations:AttachPolicy", "organizations:DetachPolicy", "organizations:DeletePolicy", "organizations:EnablePolicyType", "organizations:EnableAWSServiceAccess", "organizations:ListRoots", "sso:GetPeregrineStatus", "sso:ListDirectoryAssociations", "sso:StartPeregrine", "iam:CreateServiceLinkedRole", "cloudformation:EnableOrganizationsAccess", "sso:RegisterRegion" ]
    },
    "update" : {
      "permissions" : [ "controltower:UpdateLandingZone", "controltower:GetLandingZoneOperation", "controltower:ListTagsForResource", "controltower:TagResource", "controltower:GetLandingZone", "controltower:UntagResource", "cloudformation:DescribeOrganizationsAccess", "servicecatalog:AssociatePrincipalWithPortfolio", "servicecatalog:AssociateProductWithPortfolio", "servicecatalog:CreatePortfolio", "servicecatalog:CreateProduct", "servicecatalog:CreateProvisioningArtifact", "servicecatalog:ListPortfolios", "servicecatalog:ListProvisioningArtifacts", "servicecatalog:SearchProductsAsAdmin", "servicecatalog:UpdatePortfolio", "servicecatalog:UpdateProvisioningArtifact", "servicecatalog:ListPrincipalsForPortfolio", "organizations:CreateOrganizationalUnit", "organizations:CreateOrganization", "organizations:UpdatePolicy", "organizations:CreatePolicy", "organizations:AttachPolicy", "organizations:DetachPolicy", "organizations:DeletePolicy", "organizations:EnablePolicyType", "organizations:EnableAWSServiceAccess", "organizations:ListRoots", "sso:GetPeregrineStatus", "iam:CreateServiceLinkedRole", "cloudformation:EnableOrganizationsAccess", "sso:ListDirectoryAssociations", "sso:StartPeregrine", "sso:RegisterRegion" ]
    },
    "list" : {
      "permissions" : [ "controltower:ListLandingZones" ]
    },
    "delete" : {
      "permissions" : [ "controltower:DeleteLandingZone", "controltower:GetLandingZone", "controltower:GetLandingZoneOperation", "cloudformation:DescribeOrganizationsAccess", "servicecatalog:ListPortfolios", "servicecatalog:ListProvisioningArtifacts", "servicecatalog:SearchProductsAsAdmin", "servicecatalog:DeleteProvisioningArtifact", "servicecatalog:ListPrincipalsForPortfolio", "servicecatalog:DeleteProduct", "servicecatalog:DisassociatePrincipalFromPortfolio", "servicecatalog:DisassociateProductFromPortfolio", "servicecatalog:DeletePortfolio", "organizations:AttachPolicy", "organizations:DetachPolicy", "organizations:DeletePolicy", "organizations:ListRoots", "sso:GetPeregrineStatus", "sso:ListDirectoryAssociations", "iam:CreateServiceLinkedRole", "iam:DeleteRolePolicy", "iam:DetachRolePolicy", "cloudformation:EnableOrganizationsAccess", "iam:DeleteRole" ]
    }
  },
  "typeName" : "AWS::ControlTower::LandingZone",
  "readOnlyProperties" : [ "/properties/LandingZoneIdentifier", "/properties/Arn", "/properties/Status", "/properties/LatestAvailableVersion", "/properties/DriftStatus" ],
  "description" : "Definition of AWS::ControlTower::LandingZone Resource Type",
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/LandingZoneIdentifier" ],
  "definitions" : {
    "Tag" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Value" : {
          "minLength" : 0,
          "type" : "string",
          "maxLength" : 256
        },
        "Key" : {
          "minLength" : 1,
          "type" : "string",
          "maxLength" : 256
        }
      }
    },
    "LandingZoneStatus" : {
      "type" : "string",
      "enum" : [ "ACTIVE", "PROCESSING", "FAILED" ]
    },
    "LandingZoneDriftStatus" : {
      "type" : "string",
      "enum" : [ "DRIFTED", "IN_SYNC" ]
    }
  },
  "properties" : {
    "Status" : {
      "$ref" : "#/definitions/LandingZoneStatus"
    },
    "LatestAvailableVersion" : {
      "minLength" : 3,
      "pattern" : "\\d+.\\d+",
      "type" : "string",
      "maxLength" : 10
    },
    "Version" : {
      "minLength" : 3,
      "pattern" : "\\d+.\\d+",
      "type" : "string",
      "maxLength" : 10
    },
    "DriftStatus" : {
      "$ref" : "#/definitions/LandingZoneDriftStatus"
    },
    "Arn" : {
      "minLength" : 20,
      "pattern" : "^arn:aws[0-9a-zA-Z_\\-:\\/]+$",
      "type" : "string",
      "maxLength" : 2048
    },
    "Manifest" : { },
    "LandingZoneIdentifier" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "Manifest", "Version" ]
}