SCHEMA = {
  "typeName" : "AWS::EC2::VPCCidrBlock",
  "description" : "Resource Type definition for AWS::EC2::VPCCidrBlock",
  "additionalProperties" : False,
  "properties" : {
    "CidrBlock" : {
      "type" : "string",
      "description" : "An IPv4 CIDR block to associate with the VPC."
    },
    "Ipv6Pool" : {
      "type" : "string",
      "description" : "The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block."
    },
    "Id" : {
      "type" : "string",
      "description" : "The Id of the VPC associated CIDR Block."
    },
    "VpcId" : {
      "type" : "string",
      "description" : "The ID of the VPC."
    },
    "Ipv6CidrBlock" : {
      "type" : "string",
      "description" : "An IPv6 CIDR block from the IPv6 address pool."
    },
    "Ipv4IpamPoolId" : {
      "type" : "string",
      "description" : "The ID of the IPv4 IPAM pool to Associate a CIDR from to a VPC."
    },
    "Ipv4NetmaskLength" : {
      "type" : "integer",
      "description" : "The netmask length of the IPv4 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool."
    },
    "Ipv6IpamPoolId" : {
      "type" : "string",
      "description" : "The ID of the IPv6 IPAM pool to Associate a CIDR from to a VPC."
    },
    "Ipv6NetmaskLength" : {
      "type" : "integer",
      "description" : "The netmask length of the IPv6 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool."
    },
    "AmazonProvidedIpv6CidrBlock" : {
      "type" : "boolean",
      "description" : "Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IPv6 addresses, or the size of the CIDR block."
    },
    "Ipv6AddressAttribute" : {
      "type" : "string",
      "description" : "The value denoting whether an IPv6 VPC CIDR Block is public or private."
    },
    "IpSource" : {
      "type" : "string",
      "description" : "The IP Source of an IPv6 VPC CIDR Block."
    },
    "Ipv6CidrBlockNetworkBorderGroup" : {
      "type" : "string",
      "description" : "The name of the location from which we advertise the IPV6 CIDR block."
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "VpcId" ],
  "createOnlyProperties" : [ "/properties/Ipv6Pool", "/properties/VpcId", "/properties/AmazonProvidedIpv6CidrBlock", "/properties/Ipv6CidrBlock", "/properties/CidrBlock", "/properties/Ipv4IpamPoolId", "/properties/Ipv4NetmaskLength", "/properties/Ipv6IpamPoolId", "/properties/Ipv6NetmaskLength", "/properties/Ipv6CidrBlockNetworkBorderGroup" ],
  "primaryIdentifier" : [ "/properties/Id", "/properties/VpcId" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Ipv6AddressAttribute", "/properties/IpSource" ],
  "writeOnlyProperties" : [ "/properties/Ipv4IpamPoolId", "/properties/Ipv4NetmaskLength", "/properties/Ipv6IpamPoolId", "/properties/Ipv6NetmaskLength" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:AssociateVpcCidrBlock", "ec2:DescribeVpcs", "ec2:AllocateIpamPoolCidr" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeVpcs" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DescribeVpcs", "ec2:DisassociateVpcCidrBlock" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "VpcId" : {
            "type" : "string",
            "description" : "The ID of the VPC."
          }
        },
        "required" : [ "VpcId" ]
      },
      "permissions" : [ "ec2:DescribeVpcs" ]
    }
  }
}